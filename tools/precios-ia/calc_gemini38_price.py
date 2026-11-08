s_input = 605275
s_cache = 15063988
s_output = 136601

t_input = 1470969
t_cache = 34336379
t_output = 379189

# Gemini 3.8 Flash introductory rates:
p_input = 0.75 / 1e6
p_cache = 0.075 / 1e6
p_output = 3.75 / 1e6

eur_rate = 0.92

cost_s_in = s_input * p_input
cost_s_ca = s_cache * p_cache
cost_s_out = s_output * p_output
cost_s_tot = cost_s_in + cost_s_ca + cost_s_out

cost_t_in = t_input * p_input
cost_t_ca = t_cache * p_cache
cost_t_out = t_output * p_output
cost_t_tot = cost_t_in + cost_t_ca + cost_t_out

print(f"Sesion 1h: In=${cost_s_in:.3f}, Cache=${cost_s_ca:.3f}, Out=${cost_s_out:.3f} -> Total=${cost_s_tot:.3f} (~{cost_s_tot*eur_rate:.2f} EUR)")
print(f"Total Conv: In=${cost_t_in:.3f}, Cache=${cost_t_ca:.3f}, Out=${cost_t_out:.3f} -> Total=${cost_t_tot:.3f} (~{cost_t_tot*eur_rate:.2f} EUR)")
