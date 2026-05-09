def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8", newline="")
    file.write("Title,Company,Location,Reward,Link\n")

    for job in jobs:
     file.write(f"{job['title']},{job['company_name']}, {job['location']}, {job['reward']}, {job['link']}\n")

    file.close()