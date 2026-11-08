import json

log_file = r"C:\Users\migue\.gemini\antigravity\brain\ae0d77ea-1004-4459-bb12-8bf2643bf77c\.system_generated\logs\transcript.jsonl"

total_input = 0
total_cache_read = 0
total_output = 0
last_input = 0
last_cache_read = 0
last_output = 0
step_count = 0

with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        step_count += 1
        try:
            d = json.loads(line)
            inp = d.get('input_tokens', 0)
            cr = d.get('cache_read_tokens', 0)
            out = d.get('output_tokens', 0)
            total_input += inp
            total_cache_read += cr
            total_output += out
            if inp or cr or out:
                last_input = inp
                last_cache_read = cr
                last_output = out
        except Exception:
            pass

print(f"Total Steps in Transcript: {step_count}")
print(f"Cumulative Input Tokens (uncached): {total_input:,}")
print(f"Cumulative Cache Read Tokens: {total_cache_read:,}")
print(f"Cumulative Output Tokens: {total_output:,}")
print(f"Total Tokens Processed: {total_input + total_cache_read + total_output:,}")
print(f"Last Step Context Window: {last_input + last_cache_read:,} tokens (Input: {last_input:,}, Cached: {last_cache_read:,})")
