package com.papergenerator.service;

import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ConcurrentHashMap;
import java.util.function.Supplier;

/**
 * Background job manager for async paper generation.
 * Mirrors the Python _jobs dict + threading pattern from app.py.
 */
@Slf4j
@Service
@EnableAsync
public class JobService {

    @Getter
    public static class JobStatus {
        private final String id;
        private String status;       // "pending" | "running" | "done" | "error"
        private Object result;
        private String error;
        private long startedAt;

        public JobStatus(String id) {
            this.id = id;
            this.status = "pending";
            this.startedAt = System.currentTimeMillis();
        }

        public void setRunning() { this.status = "running"; }
        public void setDone(Object result) { this.status = "done"; this.result = result; }
        public void setError(String error) { this.status = "error"; this.error = error; }

        public Map<String, Object> toMap() {
            Map<String, Object> m = new java.util.LinkedHashMap<>();
            m.put("job_id", id);
            m.put("status", status);
            if (result != null) m.put("result", result);
            if (error != null) m.put("error", error);
            m.put("started_at", startedAt);
            return m;
        }
    }

    private final ConcurrentHashMap<String, JobStatus> jobs = new ConcurrentHashMap<>();

    /**
     * Create and start a background job.
     * @param work The supplier that returns a result
     * @return job ID (UUID)
     */
    public String submit(Supplier<Object> work) {
        String id = UUID.randomUUID().toString().replace("-", "").substring(0, 16);
        JobStatus status = new JobStatus(id);
        jobs.put(id, status);

        CompletableFuture.runAsync(() -> {
            status.setRunning();
            try {
                Object result = work.get();
                status.setDone(result);
                log.info("Job {} completed", id);
            } catch (Exception e) {
                status.setError(e.getMessage());
                log.error("Job {} failed: {}", id, e.getMessage(), e);
            }
        });

        return id;
    }

    public JobStatus getJob(String id) {
        return jobs.get(id);
    }

    public boolean deleteJob(String id) {
        return jobs.remove(id) != null;
    }

    public int size() {
        return jobs.size();
    }

    /** Clean up finished jobs older than 1 hour to avoid memory leak. */
    public void cleanOldJobs() {
        long cutoff = System.currentTimeMillis() - 3_600_000L;
        jobs.entrySet().removeIf(e -> {
            JobStatus s = e.getValue();
            return s.getStartedAt() < cutoff && ("done".equals(s.getStatus()) || "error".equals(s.getStatus()));
        });
    }
}
