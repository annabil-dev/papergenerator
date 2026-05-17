#!/bin/bash
echo "=== TEMPLATE COUNT BY RANK ==="
for rank in S1 S2 S3 S4 S5 S6; do
  count=$(ls "/home/otomasi/papergenerator/template/jurnal sinta/$rank/" 2>/dev/null | grep -E "\.pdf|\.doc|\.docx" | wc -l)
  echo "$rank: $count templates"
done
echo "=== TOTAL ==="
find "/home/otomasi/papergenerator/template/jurnal sinta" -type f \( -name "*.pdf" -o -name "*.doc" -o -name "*.docx" \) | wc -l
echo "=== FOLDER SIZE ==="
du -sh "/home/otomasi/papergenerator/template/jurnal sinta"
echo "=== RUNNING PROCESSES ==="
ps aux | grep python | grep -E "(sinta|journal|process)" | grep -v grep | wc -l
