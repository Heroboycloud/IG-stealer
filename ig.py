import instaloader,sys

from instaloader import Instaloader

def banner():
	print("""
\033[32m██\033[0m╗ \033[32m██████\033[0m╗      \033[32m██████\033[0m╗ \033[32m███████\033[0m╗\033[32m██\033[0m╗\033[32m███\033[0m╗   \033[32m██\033[0m╗\033[32m████████\033[0m╗
\033[32m██\033[0m║\033[32m██\033[0m╔════╝     \033[32m██\033[0m╔═══\033[32m██\033[0m╗\033[32m██\033[0m╔════╝\033[32m██\033[0m║\033[32m████\033[0m╗  \033[32m██\033[0m║╚══\033[32m██\033[0m╔══╝
\033[32m██\033[0m║\033[32m██\033[0m║  \033[32m███\033[0m╗    \033[32m██\033[0m║   \033[32m██\033[0m║\033[32m███████\033[0m╗\033[32m██\033[0m║\033[32m██\033[0m╔\033[32m██\033[0m╗ \033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║\033[32m██\033[0m║   \033[32m██\033[0m║    \033[32m██\033[0m║   \033[32m██\033[0m║╚════\033[32m██\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║╚\033[32m██\033[0m╗\033[32m██\033[0m║   \033[32m██\033[0m║
\033[32m██\033[0m║╚\033[32m██████\033[0m╔╝    ╚\033[32m██████\033[0m╔╝\033[32m███████\033[0m║\033[32m██\033[0m║\033[32m██\033[0m║ ╚\033[32m████\033[0m║   \033[32m██\033[0m║
\033[0m╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝\033[0m
\033[41m=[===> Mr. Tom | https://github.com/t0mxpl01t <===]=\n\033[0m""")
banner()

x = Instaloader()

try:
	uname = input("\033[36mEnter a username \033[0m: \033[36m");print("Getting info....")
	if uname == "":
		print("\033[33mUnknown command!")
		sys.exit()
	f = instaloader.Profile.from_username(x.context,uname)


	print("\033[32mUsername\033[0m :", f.username)
	print("\033[32mID\033[0m :", f.userid)
	print("\033[32mFull Name\033[0m :", f.full_name)
	print("\033[32mBiography\033[0m :", f.biography)
	print("\033[32mBiography Mentions\033[0m : ",f.biography_mentions)
	print("\033[32mBusiness\033[0m :", f.business_category_name)
	print("\033[32mBusiness URL link\033[0m :", f.external_url)
	print("\033[32mFollowed by Viewers\033[0m :", f.followed_by_viewer)
	print("\033[32mFollowees\033[0m :", f.followees)
	print("\033[32mFollowers\033[0m :", f.followers)
	print("\033[32mFollows Viewers\033[0m :", f.follows_viewer)
	print("\033[32mBlocked by Viewers\033[0m :", f.blocked_by_viewer)
	print("\033[32mBlocked by a Viewer\033[0m :", f.has_blocked_viewer)
	print("\033[32mHas Highlight reels\033[0m :", f.has_highlight_reels)
	print("\033[32mHas a public story\033[0m :", f.has_public_story)
	print("\033[32mHas a requested viewer\033[0m :", f.has_requested_viewer)
	print("\033[32mRequested by viewer\033[0m :", f.requested_by_viewer)
	print("\033[32mHas viewable Story\033[0m :", f.has_viewable_story)
	print("\033[32mIGTV count\033[0m :", f.igtvcount)
	print("\033[32mBusiness Account\033[0m :", f.is_business_account)
	print("\033[32mPrivate\033[0m :", f.is_private)
	print("\033[32mVerified\033[0m :", f.is_verified)
	print("\033[32mPosts\033[0m :", f.mediacount)
	print("\033[32mProfile Photo\033[0m :", f.profile_pic_url)
	print("\033[32mBiography hashtags\033[0m :",f.biography_hashtags)
	print("\033[32mBiography mentions\033[0m :",f.biography_mentions)
	print("\033[32mFollowed hashtags\033[0m :",f.get_followed_hashtags)
	print("\033[32mPosts\033[0m :",f.get_posts)
	print("\033[32mTagged Posts\033[0m :",f.get_tagged_posts)
	print("\033[32mSimilar Accounts\033[0m :",f.get_similar_accounts)
	print("\033[32mPersonal Profile\033[0m :",f.own_profile)
	print("\033[32mProfile Photo.No iphone\033[0m :",f.profile_pic_url_no_iphone)

except KeyboardInterrupt:
	print("Alright, next time")
	print("\033[33mI understand!")

except EOFError:
	print("\033[33mWhy?")
