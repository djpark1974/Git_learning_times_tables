#! /usr/bin/env python

import argparse
import random
from random import randint
import time

parser = argparse.ArgumentParser(description='Times tables tester')
parser.add_argument('--numbers', nargs='+', type=int, default=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], help='Numbers to include in tables testing')
parser.add_argument('--num_questions', type=int, default=10, help='Number of questions')
parser.add_argument('--style', type=str, default="sensible", help='style: daddy, mummy, nicholas, bridget, sophie')


tables = []
for x in range(13):
	tables.append(x)

comments = {}
comments["daddy"] = []
comments["sensible"] = []
comments["sophie"] = []
comments["mummy"] = []
comments["bridget"] = []
comments["nicholas"] = []

valid_styles = ["daddy", "sensible", "sophie", "bridget", "nicholas", "mummy"]

# ADD SOME ERROR CHECKING HERE

# define sensible correct comments
comments["sensible"].append(["Excellent!", "Good job!", "Well done.", "Good on you.", "Correct!", "Keep it up!"\
			,"Great job!", "Good stuff!"])		# sets index 0 as correct

# define sensible incorrect comments
comments["sensible"].append(["Sorry, that's not correct.", "Good try, but not right.", "Oh dear.", "Better luck next time."\
			,"Keep trying - you'll get there.", "Good effort, but not correct.", "I like your effort."])
# define daddy correct comments
comments["daddy"].append(["Good show, what?!", "OOoooo, I do say!", "Jolly good.", "Most splendid!", "Tippedy top, what?!", "You really are most splendiferous!"\
			,"You might be almost as awesome as Daddy!", "Fandablidocious!", "GOAAAAAAAAAAAAAAAAAAAL!!!!!", "Magnificantoooooooo!", "Oh, I do say! How clever?!"\
			,"I doff my cap to you!", "Most splendid indeed", "extremely intelligent you are!", "Why, one might even entertain the idea that you have a brain..." \
			,"Good gracious me - you got it!", "FAN - DABBY - DOZY!!!", "Spiffing!", "Alright!!! Who told you the answer?!! Come on! Out with it!" \
			,"Well who'd have known?..", "Rather!", "Top notch!", "Fandibblyriffic.", "We may have to stop sending you to school..." \
			,"Just terrific!", "Wowser!", "How terribly clever!"])

# define daddy incorrect comments
comments["daddy"].append(["BZZZZZZZZZ. Too bad...", "Oooooopsy daisy.", "Ya numpty!", "Dumb bum.", "Deary me. You really are lacking brains." \
			,"Poo brain!", "Are you the silliest person on the planet?","How very unintelligent!", "Oh boy! <shaking of head>", "Sheeesh! I hope we aren't related..." \
			, "How terribly unfortunate!", "Dumb and dumber!", "Is that level of numptidome even possible?", "Hmmmm. Indeed. Let's take an X-ray of your head..." \
			, "Yikes! Ouch...", "You're hurting my ears!", "Not spiffing!"])

# define sophie correct comments
comments["sophie"].append(["Meh...", "I can do better...", "Psssh, whatever...", "Slow coach.", "Uuuurgh! This is so booooring - get something wrong already." \
			,"Bored. Bored. Bored. BOOOOOORED!", "Kinda impressed - not.", "Quit getting them right!", "Yeah, what evs." \
			,"What evs 4 eva...", "Mn"])

# define sophie incorrect comments
comments["sophie"].append(["Meh...", "Ha! I knew you'd get it wrong!", "Na na! Incorrect", "U b dumb.", "Stink brain...", "Clean out your ears!" \
			,"IN - CORR - ECT.", "Sooo unimpressed.", "Wrongety wrong wrong.", "BEEEEEP! Red buzzer pressed."])

# define bridget correct comments
comments["bridget"].append(["Keep it up!", "Wow! You're good!", "Fantastic effort!", "Where did you get all this brain-power from?", "Woah! You're good!" \
			,"You must have pretty smart parents!", "Mind blown!", "Keep up the good work.", "You're doing great", "Fantastic!", "Divine!", "Great job!" \
			,"You're extremely good at this!", "Well done.", "Fabulous effort!", "You're doing well.", "Keep it up!", "Keep going."])

# define bridget incorrect comments
comments["bridget"].append(["Oh dear!", "Good try!", "It's alright...", "Try again!", "Don't worry!", "Oh well...", "You need a bit more practice." \
			,"Try again...", "Maybe next time...", "Don't worry.", "Bad luck.", "Almost..."])

#define nicholas correct comments
comments["nicholas"].append(["It was speedikulous!", "OO e loo ya!", "Your kiding me!", "Rily?!", "What?!", "Good job!", "You do that!", "Mind blon!"])

#define nicholas incorrect comments
comments["nicholas"].append(["You bloo it dood!", "What was that for?", "Rely?!", "Nice trie but..."])

def hint(i, j, args):
	if 10 in (i, j):
		print "With 10's, you just have to add a zero...\n"
	elif 1 in (i, j):
		print "Anything by 1 is always the other number...\n"
	elif 11 in (i, j):
		print "Until you get to 9, it's always the number repeated, then 10 x 11 is easy..."
		print "If you get past 10 times 11, for 11 x 11 try just adding another 11 and another."
		print "And for 12 x 11, add another 11...\n"
	elif 0 in (i, j):
		print "Anything by 0 is always 0...\n"
	elif 2 in (i, j):
		print "You could try counting in 2s - 2, 4, 6, 8...\n"
	elif 3 in (i, j):
		print "You could try multiplying by 2 and then adding another...\n"
	elif 4 in (i, j):
		print "You could try multiplying by 2 and then by 2 again, or by 5 and then taking 1 away...\n"
		print "Or, you could try counting in 4s - 4, 8, 12, 16...\n"
	elif 5 in (i, j):
		print "You could try multiplying by 10 and then halving what you get...\n"
	elif 6 in (i, j):
		print "What about multiplying by 5 and then adding one more?...or multiply by 3 and add 2 of them together?...\n"
	elif 9 in (i, j):
		print "Try multiplying by 10 and then taking one away...\n"
	elif 8 in (i, j):
		print "Try multiplying the number by 10 and then taking two of them away...\n"
	elif 7 in (i, j):
		print "How about multiplying by 5 and then adding two of them?...\n"
	elif 12 in (i, j):
		print "You could try multiplying by 10 and then adding 2 more lots...\n"
	else:
		print "Ask Sophie...\n"
	return 0

def tables_loop(args, comments):
	print "\nIF YOU NEED A HINT FOR ANY QUESTION, ENTER 'h' or 'hint'...\n"
	q_counter = 0			# set the questions asked so far counter to zero
	correct_counter = 0			# set the correct answers so far counter to zero
	for y in range(args.num_questions):			# iterate through for the specified number of questions
		i = random.choice(tables)			# randomly select the first number from tables - a list including 0 to 12, inclusive
		j = random.choice(args.numbers)			# randomly select the second number from the input list of numbers
		q_counter += 1			# increment the questions asked counter 
		print "Q.{} of {}: What is {} x {}?".format(q_counter,args.num_questions,i,j) + "\n"
		ranswer = (i * j)
		answer = raw_input()			# takes input as a string
		while str(answer) in ["h", "help", "H", "HELP", "hint", "HINT"]:			# provide hint while requested
			hint(i, j, args)
			answer = raw_input()
		while reps_int(answer) == False:			# check whether an integer was entered
			print "You need to enter a whole number! Try again...\n"
			answer = raw_input()
		if int(answer) == ranswer:			# check whether correct answer was entered
			correct_counter += 1
			correct_comment_index = randint(0, len(comments[args.style][0]) - 1)
			print "\n" + comments[args.style][0][correct_comment_index] + "\n"
			time.sleep(1.0)
		else:
			incorrect_comment_index = randint(0, len(comments[args.style][1]) - 1)
			print "\n" + comments[args.style][1][incorrect_comment_index] + "\n"
			time.sleep(1.0)
			print "The correct answer was {}".format(ranswer) + "\n"
		percent_correct = int((float(correct_counter)/q_counter) * 100)
		if q_counter < args.num_questions:
			print "So far you have scored {} out of {}...\n".format(correct_counter, q_counter)
		elif q_counter == args.num_questions:
			print "You scored {} out of {}...\n".format(correct_counter, q_counter)
		time.sleep(2.0)			# pause a little while
	return percent_correct

# Function to check whether a string represents an integer
def reps_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def main():
	args = parser.parse_args()
	if args.style not in valid_styles:			# check for valid style input
		exit("Try again - check the spelling of --style")
	percent_correct = tables_loop(args, comments)
	if percent_correct == float(100):
		print "\nBrilliant!!! That gives you {}%!!!!".format(percent_correct)
	elif 90.0 <= percent_correct < 100:
		print "\nVery good!!! A solid performance of {}%!!!!".format(percent_correct)
	elif 80.0 <= percent_correct < 90:
		print "\nPretty good, with {}%. Could do with a bit more practice...".format(percent_correct)
	else:
		print "\nYou got {}%. You'll do better with some more practice...".format(percent_correct)
	print "\n"

if __name__ == "__main__":
	main()




