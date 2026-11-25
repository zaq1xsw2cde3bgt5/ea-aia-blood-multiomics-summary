from pathlib import Path
import csv,gzip,hashlib,json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'metadata'/'data_files.json').read_text(encoding='utf-8'))
for info in manifest:
    p=root/info['path']
    assert hashlib.sha256(p.read_bytes()).hexdigest()==info['sha256'], p
    opener=gzip.open if p.suffix=='.gz' else open
    with opener(p,'rt',encoding='utf-8',newline='') as f:
        r=csv.DictReader(f)
        forbidden={'Responder_1','Responder_2','Responder_3','Non_Responder_1','Non_Responder_2','Non_Responder_3','Non-Responder_1','Non-Responder_2','Non-Responder_3'}
        assert not forbidden.intersection(r.fieldnames),p
        assert r.fieldnames==info['columns'],p
        assert sum(1 for _ in r)==info['rows'],p
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.relative_to(root).parts:continue
    assert p.stat().st_size<100*1024*1024,p
    assert not p.name.lower().endswith(('.fastq','.fastq.gz','.bam','.cram','.rds','.h5ad','matrix.mtx.gz','barcodes.tsv.gz')),p
print('PASS: hashes, table structure, row counts and participant-column exclusions')
