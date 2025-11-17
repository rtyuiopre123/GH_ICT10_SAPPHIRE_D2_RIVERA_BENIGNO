from pyscript import display

club_A = {"Ben", "Manuel", "Seth", "Alonso"}
club_B = {"Alonso", "Ishan", "Manuel", "Vito"}

in_at_least_one = club_A | club_B
in_both = club_A & club_B
only_first = club_A - club_B
only_second = club_B - club_A
exactly_one = club_A ^ club_B

display("Club A: " + str(club_A), target="output")
display("Club B: " + str(club_B), target="output")
display("Students in at least one club: " + str(in_at_least_one), target="output")
display("Students in both clubs: " + str(in_both), target="output")
display("Students only in Club A: " + str(only_first), target="output")
display("Students only in Club B: " + str(only_second), target="output")
display("Students in exactly one club: " + str(exactly_one), target="output")
