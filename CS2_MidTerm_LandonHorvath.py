#Problem Number 1

class TaskBoard:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, title, owner):
        if task_id in self.tasks:
            return False

        self.tasks[task_id] = {
            "title": title,
            "owner": owner,
            "status": "todo"
        }
        return True

    def move(self, task_id, status):
        if task_id not in self.tasks:
            return False
        if status not in ("todo", "doing", "done"):
            return False

        self.tasks[task_id]["status"] = status
        return True

    def by_owner(self, owner):
        return sorted(
            task["title"]
            for task in self.tasks.values()
            if task["owner"].lower() == owner.lower()
        )

    def counts(self):
        result = {"todo": 0, "doing": 0, "done": 0}
        for task in self.tasks.values():
            result[task["status"]] += 1
        return result

    def busiest_owner(self):
        totals = {}
        for task in self.tasks.values():
            if task["status"] != "done":
                owner = task["owner"]
                totals[owner] = totals.get(owner, 0) + 1

        if not totals:
            return None
        return max(totals, key=totals.get)
    
    #Problem Number 2
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.followers = set()

    def follow(self, user):
        self.followers.add(user)

    def unfollow(self, user):
        self.followers.discard(user)

    def follower_count(self):
        return len(self.followers)


def follow_all(playlists):
    if not playlists:
        return set()

    result = playlists[0].followers.copy()
    for playlist in playlists[1:]:
        result &= playlist.followers
    return result


def follow_exactly_one(playlists):
    counts = {}
    for playlist in playlists:
        for user in playlist.followers:
            counts[user] = counts.get(user, 0) + 1

    return {user for user, count in counts.items() if count == 1}


def inactive(all_users, playlists):
    active = set()
    for playlist in playlists:
        active |= playlist.followers
    return all_users - active


def report(playlists):
    distinct = set()
    for playlist in playlists:
        print(f"{playlist.name}: {playlist.follower_count()} followers")
        distinct |= playlist.followers

    print(f"Distinct followers: {len(distinct)}")