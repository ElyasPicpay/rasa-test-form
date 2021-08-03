.PHONY: all clean actions

## FLAGS:
# TODO: This is a hotfix while RASA don't solve dependencies issues.
LOG_LEVEL = -v
webchat:
	rasa run -m models --enable-api --cors "*"
# ACTIONS
actions:
	rasa run actions \
		--actions actions \
		$(LOG_LEVEL)