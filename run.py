import prime.myconstants as mc
from prime.prime import Prime
from email.email import Email
def run():
    p=Prime(mc.START,mc.FINISH)
    formattedPrimes=p.prettify()
    print(formattedPrimes)
    newmail=Email()
    # newmail.to='soumyendu.pc@gmailcom'
    # newmail.subject=f'Prime numbers betwwen {mc.START} to {mc.FINISH}'
    # newmail.body=formattedPrimes
    newmail.send()
if __name__=='__main__':
    run()

