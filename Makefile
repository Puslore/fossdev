help:
	echo "That works!"
	echo "This makefile for repo-level activity."

create-practice:
ifndef PACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice."
	mkdir -p ${PRACTICE}

remove-practice:
ifndef PACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf ${PRACTICE}

# mkdir -p demo-practice/
# mkdir -p demo-practice/src
# mkdir -p demo-practice/tests
# mkdir -p demo-practice/docs
# mkdir -p demo-practice/README.md
