import argparse
import pickle
import fbchat
import login

def main(args):
    client = fbchat.Client(login.username, login.password)
    names = open(args.input).readlines()
    user_ids = {user.name: user.uid
        for name in names
        for user in client.search_for_users(name.strip())
        if user.is_friend}
    print("Found friends:")
    for name, user_id in user_ids.items():
        print("{} (user_id: {})".format(name, user_id))
    pickle.dump(user_ids, open(args.output, 'wb+'))
    print("dict (name to user_id) saved at: {}".format(args.output))
    client.logout()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find facebook profiles.')
    parser.add_argument('--input', help='txt file with names', nargs='?',
                        default='names.txt')
    parser.add_argument('--output', help='pickle output file', nargs='?',
                        default='user_ids.pickle')
    main(parser.parse_args())
