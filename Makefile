DOCKER_VOLUMES = \
	--volume="$(shell pwd)":"/ws":rw 

# === Distribution Normalization ===
.PHONY: norm
norm:
	@docker run -it ${DOCKER_VOLUMES} dev bash -c "cd normal && python3 norm.py"

.PHONY: term
term:
	@docker run -it ${DOCKER_VOLUMES} dev bash