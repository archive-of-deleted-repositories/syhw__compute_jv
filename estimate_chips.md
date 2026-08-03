I’ll estimate chip counts from public NVIDIA rack/system power, not just per-chip TDP, and show sensitivity to whether 100 MW means accelerator, IT/rack, or facility power.

Thought for 5m 7s

Assuming 100 MW is IT/rack power and “chips” means GPU accelerator packages, I’d expect:

Platform	Rack power assumption	GPU chips per rack	Racks in 100 MW	Expected GPU chips	If you mean “superchips”
GB300 NVL72 / B300 GPUs	~132–135 kW/rack	72	~741–758	~53k–55k GPUs	~26.7k–27.3k GB300 superchips
GB300, peak-constrained	155 kW peak/rack	72	~645	~46k GPUs	~23k superchips
Vera Rubin NVL72, MaxQ	187 kW/rack	72	~535	~38.5k Rubin GPUs	~19.3k Vera Rubin superchips
Vera Rubin NVL72, MaxP	227 kW/rack	72	~441	~31.7k Rubin GPUs	~15.9k Vera Rubin superchips

For GB300, NVIDIA/partners list NVL72 racks with 72 B300/Blackwell Ultra GPUs and 36 Grace CPUs, with Supermicro listing 132 kW total rack power and Lenovo listing 135 kW TDP, up to 155 kW peak.

For Vera Rubin, NVIDIA lists 72 Rubin GPUs and 36 Vera CPUs per NVL72 rack, while ASUS lists its Vera Rubin NVL72 rack at 187 kW MaxQ or 227 kW MaxP. NVIDIA also marks the Vera Rubin specs as preliminary/subject to change.

The quick formula is:

GPU chips = 100,000 kW / rack_kW × 72

So my “headline” answer is: ~53k GB300/B300 GPU chips in a 100 MW GB300 cluster, versus ~32k–39k Rubin GPU chips in a 100 MW Vera Rubin cluster, depending on MaxP vs MaxQ.

If 100 MW is facility/utility power rather than IT power, divide by PUE first. For example, at PUE = 1.2, the 100 MW facility gives about 83.3 MW IT, so the rough counts become ~44k–45k GB300/B300 GPUs and ~26k–32k Rubin GPUs.
