import json
from faster_whisper import WhisperModel

video = r"c:/Pineapple-Mana-Global/02_Media_Vault/Pineapple-Media-HQ/2026_05_GENERAL_INBOX/Raw_Mana_Capture/Testimonials/mike fendek testimonial.mp4"
out_json = r"c:/Pineapple-Mana-Global/04_Tech_Lab/output/mike_fendek_testimonial_transcript.json"
out_txt = r"c:/Pineapple-Mana-Global/04_Tech_Lab/output/mike_fendek_testimonial_transcript.txt"

model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(video, beam_size=5, vad_filter=True, word_timestamps=True)

rows = []
with open(out_txt, "w", encoding="utf-8") as f:
    f.write(f"detected_language={info.language} prob={info.language_probability:.3f}\n")
    for seg in segments:
        item = {
            "start": round(seg.start, 3),
            "end": round(seg.end, 3),
            "text": seg.text.strip(),
            "words": [
                {
                    "start": round(w.start, 3) if w.start is not None else None,
                    "end": round(w.end, 3) if w.end is not None else None,
                    "word": w.word,
                    "probability": round(w.probability, 4) if w.probability is not None else None,
                }
                for w in (seg.words or [])
            ],
        }
        rows.append(item)
        f.write(f"[{seg.start:8.3f} - {seg.end:8.3f}] {seg.text.strip()}\n")

with open(out_json, "w", encoding="utf-8") as jf:
    json.dump({"language": info.language, "language_probability": info.language_probability, "segments": rows}, jf, ensure_ascii=False, indent=2)

print(f"Wrote {len(rows)} segments")
print(out_json)
print(out_txt)
