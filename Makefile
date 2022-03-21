all:		run

run:
			

setup: requirements.txt
    pip install -r requirements.txt

clean:
    rm -rf __pycache__

git:
	@git add .
	@git commit -m "$m"
	@git push
	@echo "Commit sent to github"
# To call: make git m="my commit"