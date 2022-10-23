from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
import random
import array
import requests
from bs4 import BeautifulSoup
# import requests
import mimetypes


class passwordjson(APIView):
    def get(self, request):
        passwordlist = {}
        for i in range(6, 128):
            passwordlist[i] = strongpassword(i)
        passwordlist[256] = strongpassword(256)
        passwordlist[512] = strongpassword(512)
        passwordlist[1024] = strongpassword(1024)
        passwordlist[2048] = strongpassword(2048)
        return JsonResponse(passwordlist, safe=False)


class custompassword(APIView):
    def get(self, request, lenght):
        return JsonResponse({lenght: strongpassword(lenght)}, safe=False)


class exracturl(APIView):
    def get(self, request):
        downloadtags = ['src', 'href']
        url = request.headers['url']
        urldetails = {'url': url}
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = {}
        for link in soup.find_all():
            for i in downloadtags:
                if (link.get(i) and link.get(i) != '#'):
                    try:
                        extresion = str(mimetypes.guess_extension(
                            requests.get(link.get(i)).headers['content-type']))
                    except:
                        extresion = "Other"
                    if (extresion not in urls):
                        urls[extresion] = []
                    urls[extresion].append(link.get(i))
        urldetails['urls'] = urls
        return JsonResponse(urldetails, safe=False)


class instagramurl(APIView):
    def get(self, request):
        downloadtags = ['src', 'href']
        url = request.headers['url']
        urldetails = {'url': url}
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for EachPart in soup.find_all("div", {"class": "_aagv"}):
            urls.append(EachPart.get_text())
        # for link in soup.find_all():
        #     for i in downloadtags:
        #         if(link.get(i) and link.get(i) != '#'):
        #             try:
        #                 extresion=str(mimetypes.guess_extension(requests.get(link.get(i)).headers['content-type']))
        #             except:
        #                 extresion="Other"
        #             if(extresion not in urls):
        #                 urls[extresion]=[]
        #             urls[extresion].append(link.get(i))
        urldetails['urls'] = urls
        return JsonResponse(urldetails, safe=False)


def strongpassword(MAX_LEN):
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*',
               '(', ')', '}', '{', '[', ']', '=', '<', '>', '/', ',', '.']
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    passl = random.choice(DIGITS) + random.choice(UPCASE_CHARACTERS) + \
        random.choice(LOCASE_CHARACTERS) + random.choice(SYMBOLS)
    for x in range(MAX_LEN):
        passl = passl + random.choice(COMBINED_LIST)
        passlist = array.array('u', passl)
        random.shuffle(passlist)
    return "".join(passlist)[:MAX_LEN]
