import argparse
import pickle
import fbchat
import login

MESSAGE = "Hello {}, you are the secret santa of {}!"

def main(args):
    client = fbchat.Client(login.username, login.password)
    names = [line.strip() for line in open(args.shuffle).readlines()]
    user_ids = pickle.load(open(args.user_ids, 'rb'))
    shuffle = {names[- i]: names[- i + 1] for i in range(len(names))}
    for name in names:
        first = lambda name: name.split(' ')[0]
        message = MESSAGE.format(first(name), first(shuffle[name]))
        client.send(
            fbchat.Message(text=message),
            thread_id=user_ids[name],
            thread_type=fbchat.ThreadType.USER)
        print("Message sent to {}.".format(name))
    client.logout()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send secret santa messages.')
    parser.add_argument('--shuffle', help='txt file with names', nargs='?',
                        default='shuffle.txt')
    parser.add_argument('--user_ids', help='pickle generated by find.py',
                        nargs='?', default='user_ids.pickle')
    main(parser.parse_args())