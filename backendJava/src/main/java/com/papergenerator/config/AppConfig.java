package com.papergenerator.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Configuration
public class AppConfig implements WebMvcConfigurer {

    @Value("${app.uploads-dir:uploads}")
    private String uploadsDir;

    @Value("${app.exports-dir:exports}")
    private String exportsDir;

    @Value("${app.papers-dir:papers}")
    private String papersDir;

    @Value("${openai.base-url:https://api.openai.com/v1}")
    private String openAiBaseUrl;

    @Value("${openai.timeout:600}")
    private int openAiTimeout;

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("*")
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS")
                .allowedHeaders("*");
    }

    @Bean
    public WebClient openAiWebClient() {
        return WebClient.builder()
                .baseUrl(openAiBaseUrl)
                .codecs(c -> c.defaultCodecs().maxInMemorySize(16 * 1024 * 1024))
                .build();
    }

    @Bean
    public AppDirectories appDirectories() {
        AppDirectories dirs = new AppDirectories();
        dirs.setUploadsDir(ensureDir(uploadsDir));
        dirs.setExportsDir(ensureDir(exportsDir));
        dirs.setPapersDir(ensureDir(papersDir));
        return dirs;
    }

    private Path ensureDir(String dirName) {
        Path path = Paths.get(dirName);
        try {
            Files.createDirectories(path);
        } catch (Exception e) {
            throw new RuntimeException("Cannot create directory: " + dirName, e);
        }
        return path;
    }

    public static class AppDirectories {
        private Path uploadsDir;
        private Path exportsDir;
        private Path papersDir;

        public Path getUploadsDir() { return uploadsDir; }
        public void setUploadsDir(Path uploadsDir) { this.uploadsDir = uploadsDir; }
        public Path getExportsDir() { return exportsDir; }
        public void setExportsDir(Path exportsDir) { this.exportsDir = exportsDir; }
        public Path getPapersDir() { return papersDir; }
        public void setPapersDir(Path papersDir) { this.papersDir = papersDir; }
    }
}
