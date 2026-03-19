.PHONY: another_app
# not all targets are listed in PHONY

# Might be correct, but "build" and "app" are different
build: main.c
	gcc main.c -o app

# Correct in PHONY
app: main.c
	gcc main.c -o app

# Incorrect: listed in PHONY
another_app: main.c
	gcc main.c -o another_app
