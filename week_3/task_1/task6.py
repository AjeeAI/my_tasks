candidate_form = dict()
candidate_form["score"] = int(input("Enter your jamb score here: "))
candidate_form["first_choice"] = input("Enter your university first choice: ")
candidate_form["o_levels"] = [
    int(input("Enter your o_level result for English: ")),
    int(input("Enter your o_level result for Mathematics: ")),
    int(input("Enter your o_level result for Physics: ")),
    int(input("Enter your o_level result for Chemistry: ")),
    int(input("Enter your o_level result for Biology: "))

]
candidate_form["post_utme_status"] = input("Did you participate in the screening exercise(Input Yes or No): ")
candidate_form["department_cut_off"] = 250
avg_score = sum(candidate_form["o_levels"])/len(candidate_form["o_levels"])

eligibility = candidate_form["department_cut_off"] >= 200 and avg_score >= 50 and candidate_form["post_utme_status"] == "Yes" and candidate_form["first_choice"] == "UNILAG" and ,.