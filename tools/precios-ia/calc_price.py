# Calculate monetary cost based on official Gemini API pricing

# Session tokens (14:32:15 to now)
s_input = 605275
s_cache = 15063988
s_output = 136601

# Total tokens (entire conversation)
t_input = 1470969
t_cache = 34336379
t_output = 379189

# 1. Gemini 1.5 Pro Pricing (standard tier <= 128k context)
# Input: $1.25 / 1M
# Cache read: $0.3125 / 1M
# Output: $5.00 / 1M
cost_pro_s_input = (s_input / 1e6) * 1.25
cost_pro_s_cache = (s_cache / 1e6) * 0.3125
cost_pro_s_output = (s_output / 1e6) * 5.00
cost_pro_session = cost_pro_s_input + cost_pro_s_cache + cost_pro_s_output

cost_pro_t_input = (t_input / 1e6) * 1.25
cost_pro_t_cache = (t_cache / 1e6) * 0.3125
cost_pro_t_output = (t_output / 1e6) * 5.00
cost_pro_total = cost_pro_t_input + cost_pro_t_cache + cost_pro_t_output

# 2. Gemini 1.5 Pro Pricing if counted in >128k tier:
# Input: $2.50 / 1M, Cache read: $0.625 / 1M, Output: $10.00 / 1M
cost_pro_high_session = (s_input / 1e6) * 2.50 + (s_cache / 1e6) * 0.625 + (s_output / 1e6) * 10.00
cost_pro_high_total = (t_input / 1e6) * 2.50 + (t_cache / 1e6) * 0.625 + (t_output / 1e6) * 10.00

# 3. Gemini 1.5 Flash Pricing:
# Input: $0.075 / 1M, Cache read: $0.01875 / 1M, Output: $0.30 / 1M
cost_flash_session = (s_input / 1e6) * 0.075 + (s_cache / 1e6) * 0.01875 + (s_output / 1e6) * 0.30
cost_flash_total = (t_input / 1e6) * 0.075 + (t_cache / 1e6) * 0.01875 + (t_output / 1e6) * 0.30

# Conversion to EUR (~0.92 EUR / USD)
eur_rate = 0.92

print("=== COSTE SESION DE AHORA (1 HORA) ===")
print(f"Gemini 1.5 Pro (Standard <=128k): ${cost_pro_session:.2f} (~{cost_pro_session * eur_rate:.2f} €)")
print(f"  - Input direct: ${cost_pro_s_input:.2f}")
print(f"  - Cache read:   ${cost_pro_s_cache:.2f}")
print(f"  - Output:       ${cost_pro_s_output:.2f}")
print(f"Gemini 1.5 Pro (Tier >128k):      ${cost_pro_high_session:.2f} (~{cost_pro_high_session * eur_rate:.2f} €)")
print(f"Gemini 1.5 Flash:                 ${cost_flash_session:.2f} (~{cost_flash_session * eur_rate:.2f} €)")

print("\n=== COSTE TOTAL CONVERSACION ===")
print(f"Gemini 1.5 Pro (Standard <=128k): ${cost_pro_total:.2f} (~{cost_pro_total * eur_rate:.2f} €)")
print(f"Gemini 1.5 Pro (Tier >128k):      ${cost_pro_high_total:.2f} (~{cost_pro_high_total * eur_rate:.2f} €)")
print(f"Gemini 1.5 Flash:                 ${cost_flash_total:.2f} (~{cost_flash_total * eur_rate:.2f} €)")
