from bs4 import BeautifulSoup
import requests

def test():
    return "hello world"

def get_new_token():
    url = "https://www.carbonfootprint.com/calculator.aspx"

    payload = {}
    headers = {
        'authority': 'www.carbonfootprint.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en;q=0.9',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Cookie': 'CFp4CookieCheck=OK; CFp4Session=d1irkpjs22ejvw5y5ypcb2jw'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.headers)
    return response.headers['Set-Cookie']

# print(get_new_token())

def get_common_transport(km_bus = "", km_coach = "", km_rail = "", km_int_rail = "", km_tram = "", km_sub = "", km_taxi = ""):
    # url = "https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=7ed100813a406a753c01546db353190e"

    # payload = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=NYbLi%2BxMzFSeFmcQF0bZN62Z5eMMmDN38aXjpF8FeIXrVtDLngd5lcCV8DkWVAucxWDmjmDkhIXqkkrmwQ0Eyq0BjhUj43Sup%2FlgX%2BcxPtYequJg0ApB4xj1JDyUpCb4rRUNjgWTPdBlO%2BtOudyy1eiOs7hZa8N3oqDUrKcO75TOqCS7VMtvPiZMhTuSIEldQYIWcGzbecVUOo5O7ktdZiwFezQvRYuQW1b3aV6Omg2klDMGNsoqcOV3a2V1fo0yFPbr4OQN7Z60XgqOy0VNtoDfCqKsY21TM7BCjk4NAdf5hW5%2BHhqM56aR1yKmU4e%2FOcIhXm0FDfzs7j4mC7QGJMeNf9jX%2BqlLrlbAsBa5HCI5xVA64WRjhnyhn7dNqktHdSKPEX23d4cLYcue7KMHerQKMAjdppyz2mk0gs220Uf6R9eTFQWdswXm0bBaa5rKQ5yoH8LaDqGAy97Xl3Zm3mA5sUS7aQao%2FEPTlw9hOKY13%2FrZ44Bjg1APqKTgO5y9RJolo07wQFa1GEwLYU4MSbbxxUCAKJsVwzLgfRakT%2BNPAsLs5a9LtQH2Gs37wYBkfbS4TtXjR2g2oODmMtnOnDEy80exDEGBg7CqhAWXKkNy9HYHoF2mXXfyIYk0uyvgKRb%2FqiN5isJ%2FK4N7nUrjVx5PnWRHRrnTeDMVNk7VG8SJr0sEmFzcsFhyrlCbR5xlwmZXDNnrPw0A4u2E7kWhGM%2Fzeev%2BXP%2BCUd2V63TEFb%2BjR6yhCI3hkIA9%2FIR%2FOy4oM5NLA%2FYE4EJyW3%2BiBGAUqLsLY24eLzpvscK%2BsyaLwGCD9ZvGmpYleSXqSmpQYucJ438dYhL50K%2BkY4HXp87R6qVgnBCRe0IZ5J8bnLiZPEmTCKQZEAW4xPWhqQ%2FgSn%2BcYhpY5PPyq3Hi97UnYQnHJX%2FXUF0Vrw3UcamC%2F4EpEt48L0u2QMcJqItq1q%2FRbmFUAxXMacBRyP0Hp1i%2BghBcF1%2Fep5PjNh1qIUjyzUt7BzxwTmZH2V7UTHRr%2FFQe9O6zmzi7IsCCyt7l9v%2BzoUAzImlpzzsad5cAmZYGC5vq8iP60G7Ki9AFJBk1LgbjFM88GuITDpR73Tmwr0ka2y84VCuoYSaEwD1qI67xsZavWtvFbJVBTj71E4KCkGXPneJaBaL%2BskaKJ7fio4H%2B850KgRsMfjsH37n93jE8wTn9%2BEpDUUao%2FQN2hUQ8d6pephZz2Az6jokrcECRok8A2MtRx68yHPdGxTYFLcwbHmulRs%2FQ6whZhZh%2FgmIQwQMmgOJFhjA247sbpNO6B0v%2FRnbAlOLdTc57TbS%2FtiJtWnOC%2FjY7st3UXvsrGR7DwF23WvXNU1ZYdr2YdPxt7UUuOQvST1o8oVzMllCj71ukoVvZtk%2FgO6HcE8mFoY27oUufE4KbYgAraLxAffOVXjV6ks6wLOuvdleg2S%2B97RZ1VMJN3%2BtqcPE3AN6fvOkcptTHKmJXJVa%2Ba9TmzXskS6Vp0WoJjIH4D1oDhvDECPWkDG2LQBVAE1YPEM7n%2FirnXUXJ5s0CmfVS4a%2FcCPtUm5ZL7A9F2itZZp%2FvaMNiw%2Bx0EufbsYNuAVeKxVbdesowUOKEvGCd52%2FhWcjcJzdsbihonfCghaVb1UhuI0vUQdpMtnukHcC7Zeb01Ti9XnhI8mPWoH2iG%2FozYFRRieurZt3wbU6n9wUohsNsd2mrFUP4pHSkEjw4xQdgXmis7l8xyZtmBghTlV%2F2WhbUMlCM10qF8jJc4Co697MinxTbZAzPFb0CZ1h0g2YrbfItsRD88gvwkH%2FZ9dFwA6cr3tkpLAQ%2BOrFPTiQ6mZet9W%2B1eEuPO8WjUEXPO95a9zlfvh5oeGz7iJWYJ8GN7LT562AibaoVUyJQnIprQDlw7x8QcU%2Blk2Q%2BYGrUhiMh%2Bokrjw7AlHqk39AgTS12ys0gb8FvLWQYnaogKw581tBRI9U15G7FARMMbRs17B7cx6bXuvLmvUMAFVKpk22H0hIWaxWBozGCUQMsbDIhO4R7JzUP%2FfMgPM5WO7V6PMaZ%2F13oiYRNTjc33bkXDwvebnDMPyvPjPufnKueX3%2BVxYFDKZRx6WAtnMdDOcGeGEzDk%2FAVU6b1qAO6saPNSarfzAFUoOYN5JBCeqqgHFCZyijl64Q9rfSyL9oS19VWc%2F%2Bu3FYDPG8GagaWbyUX0dKQ9fVCFGlv8%2FaxmTJN9XqYnWPGlZlHlopgpkTMl2eNg1NKGiIGKt2tktgLioxR2PP7MY9hPNatKzgLetM4i6X3v6Mctni7ysbqLbseMbQzGkQcQ3%2BdsVCoizuB9tylQqOuw9bMLweeqUJpxw0KQg1ohnX2F0%2BGnmXYHYMaAPD5Woy1%2B7J2jLJQL0tePItEsQCjzTq8F%2F7O8y2attISKisqTctvoohmBzRjZGCP%2BcEcbGMFPnDZwU%2FbuSNfZLTJXS61falaxp58sfaZ7UFJ5q28hqG0febaZz1qN2ueihphG86YDfcLtb2AxVH4yOjKHq0uQd24FbsUM2iqGFm5C%2Ftn%2BSjOQXra33zDvot4DgHx2sbTsFHonGYqjdECc9dsYrAFLFaoBE5H4QSe4TvqgR0M4AcsB0m97zScnedtapLutHJEGkr8nMeDFlK4BuOT0W%2F%2FCS%2F4atPk9yXTl1E9y6mFUlhiqOSRtimtl%2Fyr%2Bmmtid8KSIePOSmPrTS1zZaSXsOPL1zVLKg45sV1DaRWdH3QCWFAtb2jPlLmkv8d9Nw%2BPiU11dOW4Y8%2B5E3MYSs6wm98ajKzOkQHKxcGAHIKcj2xmKuFP3YmlNoK7lfBAtzchw%2FMkLbiFxEtHnIsiBIKNi67ap15qeR3CDnkdE5sCzIim4SyfRqlQ1SA9j9UziSDiscBt6NiQneg0Xuoq%2B5a5fHlgoZ%2FDMqGetqmhgbiUItI3oHr5mmhJW2HFBeI1ThDE3UR6D3Tkrh0h2UJ59W1RTUNjQBFmHB018t5aWlufBCIng59r55bMcIinvokB%2FMPyUwJvK8ZhouCJx0voKY5TCZ50cOASoYgNsX6AREc78XK0NT4RWDuzT4LvibzaWmOYNcQQyXRmsnxAHzO6tGR4BByOTJkRo4wlCnJty%2FHlmRZT7nES0w5tOIKZ7RThdJyiUWF935h6DjqK1RPSMhUCQvSZjLsE79JeXPvKWDu0eakAG2idBrMT0uEt2UfWXSL3s49v6lXe%2FQlqWp2YnWx5OsQ6SfsYgntMQfAF3o2bmqq31HaQxWI6ymuePTjRCJDcOooEtfTozxHCemSc%2BMwOA08F3xmry9sNdvdoWsHk0hba8h4oVSwWZOhaVss%2Bra1zA2fS1t6D2sRvyX4Pjr5hKd48sS6UWB6AWKeIGsEFeu8ZTFguneyOjo86Qf1B5JlrgjXuMb3v4oUaoLXXkHv23SpmSvnUs8FfQavte%2BV%2Fn9%2BbuzeVScsRjrgwxLNhqvKxv%2BS4CA9EymRr7NNJ1meELL3ztO5YpM%2FFP7IFPeKIGWbLuGC5sr982beIpaDs%2Bu40A83H4kQzjYHQGwuZt764S9O3gejl8wA5eFkI7QybzDfVLGA23N%2BOYC2mE7iklzhjbUdclzvoQA%2BU5c42qM%2B5pFNFMotAehy5dhvxD27oPa3d%2BF%2FnDmv%2Fvng6px%2BVHGp3Q9KbezzkKQLdMNlq9e%2FN3Wt%2BzF9zkpL2pC5YeOLs9d58ohT0CPTIwNOmHDQyPllIHxPomDGJU3xf4CJsImMjgPv5ZqiAvSRPCAr%2FkVXlBmvMsqUK9sb8AS2AM1e6HU0yFZvfZBGDkFOSQ2MKntS8San0GU6%2BYkoT3JfFb7CteNQzHzsYymVQLEzyE7Ki0RjKP2imBvyroUkM5%2FZ21kjnl3sBo8WZnoRZFLTKUs36TnCRswAhCiNJ4gu82miII04y1%2BuhIg%2Fe5rvdFofNxf3qmeC5ca7HuyEksuvoOT6LWhPMkvePQ0Tkl%2BCsnc4gm4aG5zYsAi%2BAST7aBZeF4Uk%2FzKqe7kULzNf2xXOKccfkZuKQuBjAgISPdxCQS15k%2B%2B%2F5LwqYITucRjJo0e%2BmVtQcV3yk%2BQrFs%2BZEUKwdBwhcPfD0Th7tm1nM5LyIASu2wBMZikREJXkKxC1l33%2Fik7%2BEe49eFJJhNdmsCrMwLNzQ8voWzZoCdRv%2FHVS5U8K7oWoE7uzDLnzyrDZiEKeOehV%2BMixvsnTR9OspJQ0r%2Fk69dsx1Qxxar1I1xvfRxPYv%2FWW0ZGsxB448xfBJZ5Atv7NxXa3eJ4nkhmeWvMs27wmjOXl%2BUJjBtxAdU0NDh%2FV%2BxLU%2BzcH3rpbivg9dWlS%2BqSdGcKHpv%2B2FTPB%2BG1I0rKJvhvbYL7EkVyBdd%2BFtbJbsgh7aybXmecgLw3d0hThsTbzoiBgE%2FL2F4iIvbNsMvBnmQLW2hCZp6o7oaqxLMDTpunv1wg%2FK5wCNmxzvTPhe567OZ99bvdtKi7%2BKBduvFeV1XFC04S2zqMszXlMf%2FY58pCmx12iExZJlyUy2hGhhdySbHn5LtQdqdGtSmP7NIIvHBrU%2FAuYPE%2FzPHvFS5o%2BVYSmoeCIx2J4lyIchxIqUkjEVxnnJ%2FRalulb8yteBpIFKRdrF83%2FGxqzaQm0qGWccWUxONO2kSak3wst75KOPoXJeZtLiODGbu2kIIrW%2Fw%2FZYLWR%2FAqYANpOBQhwYqvS7nLR9uMgi44qpfpTpGQnTR%2F3VBrQb3MFkQtW0JpahvO%2BMHHfxE6zhZ0e9aoaX8fhEDvCdqmyJqynqxvOwvkoBxCyf4Bj4qG%2FP0JCJGLdUP%2F0aqSIpLPexwBash%2FjpLcL5M4b7pRP%2BAF4%2B%2B94TI39IL8TpRpTIJHOCjUlYN7jWOIc2UL%2B7rcgSzocjX9ZFMrY5CxHVMjEyzj9JTQCU6pD%2FO22gKd%2BibbbtCoh1tEeO3IFfmy1pcc49zqucOYxjJLls%2FfUChllv5OW3RfGJqkvnJAqEbZXqaWdjRyIO2kugnFXk8KnGEJwAattgNX7HIEX%2FvbXwcmjruFWIuKtYWx8ufhJw6CzTZIc6TxtZ93YckpUcYmrR8rUvQ40q6dmugqbEkDA2cv4vugl4DuqKuGoUZG2tm%2FcBGGJ5xNX1OSTmP8J2LX7zS2TLmRxXYmSjAgBoCvqYo%2FTHGxIRSjjuDJQm2a1b%2FDnyU%2Bg5L9wGod5g2PtboJB1XynIn4Ctn13u2fpCOXIgP%2B2DA7K1ezMLECFMUsoao67u0toP0m6GAMxlXE%2FHpJg6h8AHHHKh%2F8bw5Yp9%2FfZ0SzlEUA2KY9BEmgAcAtIH%2BzBzrOunexxq2tAUgaGMSJSb9eeIae%2F2BbzWVZw6FygL2LXM6Eg%2FHeVFF25T6MCHA1mav7mqSOYuIn5ONrXbEWYZMT2J12GY8iWKF2peGYn8RgEbiK0NbKmMR5l0F%2ForteJeaNWB5QsvZBEeJxr3QhyltONOzEt6NthBllwZO6ht%2FjBjJmQodcF0%2Buf2OGO8hRWVu7wEjmADHqwSyVv6VJkG4zPzEtF6eXL2GVN2f5p12%2Fze50I0g0ebUEf33euujBXOZMLOIJN7JbHbYs7U%2B%2B6y9jAVKNkR3tcxCaw5cirdeGcsSUANLK%2F585rpxuZoiVAQZ0AePzt%2FngZWGlSq%2FJPxQwT%2BR9%2B3FFge1DkSSoqD1N2tTAIesr7qfGFb1pCAOhypCPRu0yyRIGDrq53Xk7rB3rWzw55xWiFYH5zDXHUUI346T15URWPs0FerhncsJnQAP0dN%2BX%2BxqFQBO7PCJ5csfGP8xFKO6joxbAjm0VdRuFOXHyW5Nqs943azl%2FPEmpmLMUcf7Hdzeh1spagAnzIM%2BzAXG%2BK57CwtQENu6jZiYi59LxSiMapC2kS68Y%2FDYxiynDdWlq%2F8SXgG4t6WuqAqUz4RQ515k5dvNxDtuj4AwYEsgII5sV2wzQG1%2BMZz1UJbJcTmTy5ZctWFoFstlYkta1EYZuXN6qbU%2FBvg2kBKEDIBd%2BOKz8sVNjjzIdWDllKNwHQtBBhJn5ILNX0pxpkWTRViwX7qn9Wqrk1wti6t4o%2BF%2BWiXzhT6E2ilwjWCBfzwAvtg9wSSRljRe1aIbUfbX0IXSwCwItG1ljoke3KZicyIxLrJoBlS7E2AqE5nT2awJlcY%2BYbjehnVZtPSYr%2B97bCF8Jomnee90EBcJCQKgJCcP%2FfXH5YXoLI4KZe31vhSEyTrj48VRGocCoeuT0ARb8O%2B3T%2ByQhLVaJUq2EaX%2FgVlpLnWdhg1Tu%2BZNoXvRLan94jildfHCqWh0ojRPPTMqaR8oQ1Td9Svp%2BsEwGksu7xSdi%2FmS%2Fb7bB1JpykNvdjpnXjOIYoBsEWCWD%2BJbyENZEUzV4C22JNdaDscJfWIYqI5ZvlOZJw3IREo2F0%2FH2b63pb%2Bmvp2yY%2BkPvjhQoTPArYREZ2qmTqqdM7QYmPqREPzwYexQMGisdi1EaDVZNRhifBLvOfcPYmZ71zkmWhnVBI%2BvvD9lg3Ae2mZIKTUymfZTqoawom%2FI1JIeV9UVaP0R0mzQcDYReRcO%2BMiwUINVrwQHwEkRlcGxWASSTiy0dazc776RdGph6Eknx%2FC34b27%2BzhqZKD9EFxpyjXSdqlxFGTcJ5vnZaGGcIJkZWL3BMqma94grfC%2BLX62chLtnmfjnbvSDAt%2BLy%2FPoqm1G5xLIAhsWO3fmdjn0Tl0nFgzoGkFS6mAo09SsIqAXKsMDNogEPbmzCo3rwqcY9ht07tVh69xTC8IGjHuDtRzh%2FG74Pr7aN8IS7gOhc%2Fja4nwiH4YjAvgjBgR9xCsqQJYVJl35kUNlP0tynmjlHrImu1ro9U9rlhL2pWcrlmVCaDnwrvMEtEwnegY2aemQ2HNrmJg4bh%2Foj8WGLFUej9sUD9cX8qZQlauiFrFlJq9tp%2BdO3aGoCuwpVxf1JBohZIC0u10GFA1q7lqOtGqPcgDxX0bEO&__VIEWSTATEGENERATOR=10DAA136&' + \
    # 'rtsCalc_ClientState=%7B%22selectedIndexes%22%3A%5B%225%22%5D%2C%22logEntries%22%3A%5B%5D%2C%22scrollState%22%3A%7B%7D%7D'+ \
    # '&ctl05%24cdsBus%24txtMileage=' + str(km_bus * 100) + \
    # '&ctl05%24cdsBus%24ddlMileageUnit=1'+ \
    # '&ctl05%24cdsCoach%24txtMileage='+ str(km_coach * 100) + \
    # '&ctl05%24cdsCoach%24ddlMileageUnit=1'+ \
    # '&ctl05%24cdsNatRail%24txtMileage='+ str(km_rail * 100) + \
    # '&ctl05%24cdsNatRail%24ddlMileageUnit=1.6093'+ \
    # '&ctl05%24cdsIntRail%24txtMileage='+ str(km_int_rail * 100) + \
    # '&ctl05%24cdsIntRail%24ddlMileageUnit=1'+ \
    # '&ctl05%24cdsTram%24txtMileage='+ str(km_tram * 100) + \
    # '&ctl05%24cdsTram%24ddlMileageUnit=1'+ \
    # '&ctl05%24cdsTube%24txtMileage='+ str(km_sub * 100) + \
    # '&ctl05%24cdsTube%24ddlMileageUnit=1'+ \
    # '&ctl05%24cdsTaxi%24txtMileage='+ str(km_taxi * 100) + \
    # '&ctl05%24cdsTaxi%24ddlMileageUnit=1'+ \
    # '&ctl05%24btnAddBus=Calculate%2BBus%2B%26%2BRail%2BFootprint'


    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    #     'Accept-Language': 'en-GB,en;q=0.5',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Origin': 'https://calculator.carbonfootprint.com',
    #     'Connection': 'keep-alive',
    #     'Referer': 'https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=eea9acb70fc98a2e61711daa19c1c48e',
    #     'Cookie': 'CFp4Session=uc3cn1hro3bpq2jqxzg41dhk; CFp4CookieCheck=OK; CFp3TextSize=0.8em',
    #     'Upgrade-Insecure-Requests': '1',
    #     'Sec-Fetch-Dest': 'iframe',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Sec-Fetch-User': '?1',
    #     'Pragma': 'no-cache',
    #     'Cache-Control': 'no-cache',
    #     'TE': 'trailers'
    # }

    url = "https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=eea9acb70fc98a2e61711daa19c1c48e"

    payload = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=Qxo1bynXqUUBDxZ8Oo8KQFgvDyG4ZnMF%2FENj4LKqe8HEKHyHcyZxRtv417Rt8YnErTCDSmzYGVdHnd2JeOQrwMn4dbt6BT83YkYA0AUAaqGV3c32gGS%2Fs39SMbJ7ga5ctLcesaHRAm0t%2BOdQCB78yj9EyTtti0YKCNxjOkROWEYce4h72DS63XukjY3K5kFgxHm7iiatUcKetMB%2BmhI9yM4XrkBe92Mrskt5EE3hxPsD4gTbmhNPFxCwW%2FQDRkCwVVSxXuBLvarEC87Uf3j8drbinw2QEF0xAUy30CH5IaW8RMlng%2FqQroUxfnnaDULTISFQszipjOqsqwD99RJ1alC0UXRMYVyDRbQx9ZwwxNMReTCP3uaJLg2K5MCkIPPLZ9lHR%2FbQP9qY7uuGbih1dwx92Db%2FhZVd%2FpVj8M4vEydPvLk3nsEU2WFOOoZFwl2Hlk55M2t377JMFMEDgGx%2BS6pweOeK%2BVbHDooMYMzlHsXA5y0pHruzk7Z7aV0%2BfSjiEwIpTXNec747FTjVX%2BtiQujT8o1z%2FyJJnfxq5GPIZzHsPoCCyLJvqZz2EZ%2BM5nNCrHdODPh6Z3kFgLC9pCUs8cyRAzDdZzXbS2aqvgArPNMMn0Bs9Tlv12322ZbjA3RGsR9txVjFd5g2QzWNiPhwQ7QEdBfCIs4gSizEmUtu3M05ViJm7jeDSmHyKsswA5Rk%2FAFHPex9TiP6AzV6Lt2TPsccztdZx5EXeO9OBAZ%2F0HjsDORJ%2F8Ghi0xXwokrW6YDiICn4ewJhBOlbQVCUrw2gJLcBSMPWqgeD70Yw5mJPbKlWjoMGMFiyDvP4FOYvngVTJALZFT%2F3r7sZhcXS6gHnRFjreA4kP4RoAybQfEPFCBxUxDs1nBnYyw1CGDDPD%2FLynmE%2BugFoSBxanjE4Px2MJFCoLmk1xR2gDBj15tWAcDlZdyHzftJtPbRwztkrbYp%2BX7GAntu2CZWqXWgPfjGSIMQGAJnRNQh2N8TCsSnIL3g1l8gii13mfJ%2B%2FOCt8mvXH1xPEO%2FIrjIe98rKJkXQB8aXZ09VSAAuy2dfvpfZRsRXj%2Btud%2FTKElRzJInSmwT1ghWD448L4eWGztmaeikDBbuGAmCiSoIlSh6YJhErR7P92EAJNy5aIWJpi06PlwxHoM7nwQTUBacwCfaOf9D31bKdl2Gg26P1PBjnXdo9w2b%2FmKUDlwpiaTjKJZrCwUlN9v3LJ%2F7FT0KQc%2B7N6mtuX84UKOIT52M0sFjbusx9SsKpRDIYH05LL5J%2FVH9d9R0ZNwiyPXhgEaRd5IJPhYEOmZ4miGFsWiPq5gxNHeOsZvuYjEvA220FeOdQFdZFy1k61q4mcFl65dtakwF9UcnJ6s3NBQt35AfntYoP2PZPKmtCExur6Ua8zEXq69otLBSShZ%2F0qllM6AQiE6KH0NW4N%2FJgs%2Frk0MF%2FEsDXspnjRGTUSqZ5IOMo5wujZ8xhfzC%2FjfSh%2FQHSsgtKF1YL962WFcPKO4U%2ByVGJgis8%2BNp09N6cBpcyuMJf3uiZBwM0EqW3Mcvo36GH0B7V%2F6rpu77cT8ngQ2cD15ZlWWimY0xU7E%2Fj74K3%2B8vKMqIuHGAM4xOk5Ih215N3TOBbG4EOOmJOxRr4YbgsWpRBvtgFYN%2FZ6A1zyIs9XTp07UULN%2Fv%2FZZyVKI9If2JHclOBwWBrZG1%2Bfn0z9jzwM8%2B4r4RjCG079y4lN7%2FwaxTcyFL74qPQB7D9wS%2FfoU3o1Hz7bAymFwI4OoRe4s0lzVRMDarFlMH1OlhNUbqFxtsCLFqdTURsy1ALCuLTKzKGnMR8P7hucLF2%2Fdmx53GLwptuU%2BPwpBYZtG%2BbUdgWuk458%2FiN0vG7Sw3L%2B4igXPEwwMHA4GK%2By2jMJN0kv6jSkldhTId2W7rIgpAD8Z7OTflQWPglIRUq4JheY07Y6VJl8xovsH8FeITAsAMZ%2Fpezzx41UGJUn6RBLda737H95UYo9OmP%2BrkZFUmxVCm3s4xQyv9vCJluJ0wkFap0X41KT7xIA6Edy8WkkQUJ3fzNKA7dlU7R7SInlQAcEY1EVxVrqvOgNBgP%2BhKfSLPzeWSnlVa1NfATjy%2FZnZtltR0aM%2B6e37xJzqcMTNYM39VXOegWtAjOxhky9a4kIS0E4MSkfMbn2G3qb4UYsrei4CCJA5Brv7aossWtinYnVPJPnmFIP2Y5pnGSCgsfkkhZO5ZqbcFeG1KuXx97SoQieXkViIZ4cl42TB6IOE5Ht5I2YxHQ1pBxh0auKvi7KVru0XOXOjGyx79nCngRqoQGzjCKZT5J36opu%2BJIK0l4Tkul0%2FF07uH5YZgg1LlwuIqqhZv6j3ogM4KCusyLWd4jUVYT0QonTQOM40TTkz5ADvb82%2F0DQ632Behqqje56mLcwwLW%2F6ywQNAmUue7iBPbHm%2BJqCQwEH6%2FIRbc6oMTXD%2FL%2BeuAKN6iorNd%2FCa8%2FtD5FcbrVVHzFgyG3bCZ%2FWBT%2BmfF%2BxBaKTcJlMmb8d74N%2BNigCC8P94yYtIBy48P%2FzH3BwW2vg8%2Fj400trAzn02belmnbeOZR3IT9neRw%2FInybZX93KsIMmq8myMXcLNXu2EuVmCrFevWbgLfFwQGogJSENSJWLTdjs6M1t1X5oFKRHVWXHA%2BVBPNypG4K0Saldy4iNrEziDxf7I7FJMZMErO%2Ftw7mBgB%2FxB8YX45WgErdgYdpuk9DtdPCLd9oTs90b5ULOc7v4gyNMwBmJtcUVAq4%2BtoYyFyvZd32SZv%2Buz%2BL%2FhjXJcOq4N2G1Kn7EM2aOav%2F25iEI%2FDhmBYEWYel%2BwpjCb6BxKqk%2FRCfOjO0MdDiCaTlWzXAtbeSlm3RdP9Rx0l3i3I%2Fv3XMhGA%2FP8FkYGdNdGmL%2F68UL7oxN6CI1MUHrMUFv2My4ylH4UlwJ6nKRWiCbO3QIKQ8ofV82C%2BW%2BdPayU3imdAyFcNiGfpltaie4T3%2BDa6ykI%2BYNqaUCC0eh39wgZ2qQZHURYaBwGADc%2BDhB93jhmwlLGXB3nBz6Fq7DliB1iV6SwvC2QtSD2A9Dveb6IRTRTmpIQZ84G8mcQn4%2BjqEz4GO%2BooizCUKNClh3bDA9Sz8sBOxy92ccHr9v5uwSfPjUCKXVsoF86bUJszp8pCZJ1wyb2o1730GFgK%2FxSM7JT%2Ba0sd6PBjeXomaXQq4ewdkbU9pzPJMyHPRUegCwVFK%2BWqCeiaUpghc6QA1u0Vi%2FBK2p3YOriWw3Zb4f7Vy7JTt7TcJPpLXCeNXlRHX%2FnyNYq3LCezsYQkNJzSzRnFCLG0R7o0oH3RBdIMxQZ%2BdfxmIoNSuC3y9ZJHz9CUNnXitWniH9yhjcvJ9pzG06KHjzuEmHo30HI5A03pdGkMFC2cLDUBsav0ykl69N9vb45sdcGHwG9vDirUVyGI59BS6AiWG2xiZxtNGOvf9CDKqG6Kdh%2FgtQtFfr8PUgeSlCXSp40uzDzWtcTYm6uDXGuPV4ItkPG0plX5Lo3hbx64VS72KsjZQYZmdZIkvFEz6RfF%2BYpp0oh5VazJH5kdj2zDzBlBoR%2BrTQsJADXGQAHw9UYjHZeNj1Wn7YPFFZnK13S7GHf99RdFGhofVscma3LZ957ZWzYCSbkFuzPnF1iSt87bXxqmlJmuCfkTL0e%2Fq%2FwcqgVUCB%2B18QSSnKgvebNgHGejXnKKECHyVwAabnVXhw6%2FP6s5b%2BDmLPzuVgRRFiRGy%2B%2B9QBlQj70VQBVQYDfFc4NgE26nTGw7GkVSZwwyfqZG0GaLBQbrbcBj3Yxu1wGE28x4GtVUu1Iu4wXS0HPYk8HMNcGaS22e03miH1aPDt9MQCMyjwA3xDX8BlUHTOdBy8TUHG9FnH444ukbkM1k6V%2FI%2B5UJ8eJBf8zbs8KHYWLQbtUV5POM9kjdG9YRmnHuBUU5w2AsxCKkYT9aSVsZnJ3Nw6n89HAX10Ee0xdLFbvM67fyUFYbW8vgUKtCEUXEBzq2AhbwcJfPTC%2FS56e5Fvmqu51Sb8ZLup8vnD1wrbowWK08tJAcvU7TyHSlusCZCQKFXWQeu0j0PmB%2B8nENUAaR29vJetkkEucLcbEqPoyvd8dTyYuNLbtafk8nZpMz%2F6UU3u9H1DzpJNegZXAxGx1rZxeVns9%2Bjlh6T7MewnzxNL1to1iZUFhuDmPOJh4j2KFq7i4aBhz5RrH%2BU5YKe9P%2BfLVhvt%2Bf7qyzFtIZHMnITEaWxIW0fmxhfoPhk8%2Fpq3ZPAd%2BljJHEFZE0Ri1opBgkF2OXf7gxa7CqJ1MsWzhQFjQmZHYrFEsN6wE2VdHBmANyZ4YEZwDrtsawlGLC9x1MOJD7lKjJqrH2D32HqiEbvzdhyjE4twEUb7RWeHKQPuPlu5KUjaxuxyDkfE2lfB3H6GMfn2%2FYyHiR%2FNJ%2BsbdqQpgLc8BpUKz1zqf%2BuXuBlMZrtrERADvPYvu%2Bpa%2Fr1YirsmyUD4nNglnSycQ2K5EqveitfUtZdVnamgSu7VglJ3AqyuopAaUVF2vlrUKnSbfBPHtH6dZf%2BTEhOUHBdJmXeKiEgmoW9Ss7KXQczWVrFgk7C7l3hTpw4mmc1KdCsKHnkxG0UX2DFizJkw1YZqBPZbMZH%2B3oScVfVg1cmiyUiELlP3Mm%2F0RXbjrFmTJfdnzHR7LTOO3EK0tEJG4b6UngZ5QZyucuI0JNWC%2FMi%2BQ3pQl7H28nEZhH3YqvTS2qHy2qh1AzC%2B7XRyxgkOgPpvZTZ2WnackH%2BfCoEAL4YVkSE0ljh6ZYdDubd33E7p0YOBa%2FxnXkqRFj7anTIr3Ayas%2B1fcKuaxD8Jj29lZsC48sy97kKm48cjgGKa3lUed1Ag8Fg3kZYUBV9hIYQZr50wRs7WcRY0SKq1OAnH75LaBnaB%2FyPtJPPq3hYYE8b9B2TF41gzpXCTgGJA08oXPdBoYkerY5hHojYGDPyD7OPCXpSqoGAJgTlbXUQm4dFM77vGSiL4PrKh4nFDIraXmXp0PsCP1MlO0Nfs8OT%2FHCrca26qqbsVYWsMjZl6xQhIEPK%2BP%2B98vlVsXqHQ5NRxTO9tLM50fMaCJGmezIhOQIwC0cOdTtIjvxDRIFEbx4ga3Oa7hSc2qwE7AfdlFRwnA2G3FbhNGzOfIkb%2B%2B79S2E0cSyCuJxF1ReQn5svPHWn3KulY9Es4A1mB15HiuXWpNU4GgXGexLXAPrm4Z6dvNnMf5B3vlubDLB4lPwuXj85eyJphImraoh58xsYBIJa16NjuqJTid1cAVy6uRAEK3o0EMwY0Jizxm%2FLBCM1LWU7YLZUJYCizVUCgTOhEVIr%2FfGDsK%2Fb71W3Zl0HafVuItG9IR2PAAJdEjajUmcGttKyIuYgPyAbpDtPiTwv%2BO3ove8Cyl9hAuasssPbZdjFXXNQYeqtZCQl6q50cTZro6EL9BMatSgVAbGd1BdGrUMoGXYUJJuKtlHGaS41HTly4uoHEkuj4WCQ460qVVJziHeXdCuNMQmnSAoB5ppJbv4QDX1Z%2BTgMJfKg4Ximd7zGboeg%2Fb81%2FxQfg97Xr%2BzzoRtU6CbUINObJSFEcIm1wFRptqGzMHl9nxWhXLfbLFZtINQ%2B29Nd5xehUjf7YOgktsVGMTv1QbXNYOFe%2BKmSmBQ6ummK1QVjuLrR54cKr%2BQP7xjM1UaNs6UnpkxvtMyDToo8WxJFYB6svYaErIcT9zMvPaOX0EcoL%2BEj4SPZ3hCOa%2FLrDDojit%2BHRITpZP5omjPCG%2F4Z%2FBqFxWmA9Gcsuoo%2BqkwbEuf0eZimiiZExde%2FXOJl6OrlyBoC5snHNAG%2B7P6J0Z9U0nOuXA%2FhrQMqRq2Es3gDDWFN0MqWVzmrNUtofuX4vAK4nlWnZ%2FhtM5bMY1VqsJHjB7qYnbLKhPITfJoXXXlCtv1OGtNui%2FHb8Y%2BwRIkcYAd%2BDu%2F7%2BSoOh9QkUhkroiJpO6dkHwzkd6wxtmNMFE3%2By49cOF3vw78fvwzYjkstxueLbugDnH19vWw%2FkjKJ125APptb%2BgVEXPBQlGSFSHQdJLHHJ2Fx3TSWIFS8I4QSXr2slgPj04LLtnMjFYvVcID7axjPc01hP1vYu%2ByTIoArnrWiRt83tPnGJ4vbQ%2Fe7M1s7qi%2FkfNLGE%2Fsicn9XwGfkw4X53voeWBY31BBS78%2BdYkVcQJxo2HkBmo8UYT1HX5229iVU9lcfJcwnXNlfVUNIdjFCP%2BhVKPQYHhZ%2BhuYO%2FEcqOCOb%2BlWR1koZcL25rIJOLJqV0VhIIBuBPJtQcfXkC4YvItwk%2Bu3hXXikWmkb2RUk1B7ws1r%2FznrshWASP9gmZgZw6hwgWvBSQ0egytpgWyAxmbuMZShIXFet8IOw4yZXB4byJSLfMjhqwXbFL%2Fl8Rr9ms3wQijMYuiOGgjQuab39tR2G7ho8AVn1MAPteLFxqu%2BOqo6c38GYUZADKjV4%2BzBYwlo9%2FqaSB6gRDkZHsjdQi2amzMWhzHzib4w4aCLnjICyKK5gHx86PGKMIzl%2FtzYG8jX7HXN%2B6Gps2skaMjIe30uGz4EqMzTbW6X8pbcPZ4y5FDgEfxCkxKONxpJAFaQa6ZcSOBg2IV5k9EcQ2pr%2B5v8qj1spg85eYf7acZrPiM9Jo2iJmso%2FbExt56&__VIEWSTATEGENERATOR=10DAA136&rtsCalc_ClientState=%7B%22selectedIndexes%22%3A%5B%225%22%5D%2C%22logEntries%22%3A%5B%5D%2C%22scrollState%22%3A%7B%7D%7D'+\
    '&ctl05%24cdsBus%24txtMileage=' + str(km_bus * 100) + \
    '&ctl05%24cdsBus%24ddlMileageUnit=1'+ \
    '&ctl05%24cdsCoach%24txtMileage='+ str(km_coach * 100) + \
    '&ctl05%24cdsCoach%24ddlMileageUnit=1'+ \
    '&ctl05%24cdsNatRail%24txtMileage='+ str(km_rail * 100) + \
    '&ctl05%24cdsNatRail%24ddlMileageUnit=1.6093'+ \
    '&ctl05%24cdsIntRail%24txtMileage='+ str(km_int_rail * 100) + \
    '&ctl05%24cdsIntRail%24ddlMileageUnit=1'+ \
    '&ctl05%24cdsTram%24txtMileage='+ str(km_tram * 100) + \
    '&ctl05%24cdsTram%24ddlMileageUnit=1'+ \
    '&ctl05%24cdsTube%24txtMileage='+ str(km_sub * 100) + \
    '&ctl05%24cdsTube%24ddlMileageUnit=1'+ \
    '&ctl05%24cdsTaxi%24txtMileage='+ str(km_taxi * 100) + \
    '&ctl05%24cdsTaxi%24ddlMileageUnit=1'+ \
    '&ctl05%24btnAddBus=Calculate%2BBus%2B%26%2BRail%2BFootprint'

        # '&ctl05%24cdsBus%24txtMileage=500&ctl05%24cdsBus%24ddlMileageUnit=1&ctl05%24cdsCoach%24txtMileage=&ctl05%24cdsCoach%24ddlMileageUnit=1&ctl05%24cdsNatRail%24txtMileage=&ctl05%24cdsNatRail%24ddlMileageUnit=1&ctl05%24cdsIntRail%24txtMileage=&ctl05%24cdsIntRail%24ddlMileageUnit=1&ctl05%24cdsTram%24txtMileage='+ \
        # '&ctl05%24cdsTram%24ddlMileageUnit=1&ctl05%24cdsTube%24txtMileage='+ str(km_sub * 100) +\
        # '&ctl05%24cdsTube%24ddlMileageUnit=1&ctl05%24cdsTaxi%24txtMileage='+ str(km_taxi * 100) + \
        # '&ctl05%24cdsTaxi%24ddlMileageUnit=1&ctl05%24btnAddBus=Calculate%2BBus%2B%26%2BRail%2BFootprint'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://calculator.carbonfootprint.com',
        'Connection': 'keep-alive',
        'Referer': 'https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=eea9acb70fc98a2e61711daa19c1c48e',
        'Cookie': 'CFp4Session=uc3cn1hro3bpq2jqxzg41dhk; CFp4CookieCheck=OK; CFp3TextSize=0.8em; CFp4CookieCheck=OK; CFp4Session=uc3cn1hro3bpq2jqxzg41dhk; CFpAffiliate=RADsite',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, "html.parser")
    co2 = soup.find(["h3"], class_="nomargin").text
    print(co2)
    if co2 != None:
        co2 = co2.split("=")[1].split(" ")[1]
    print(float(co2) / 100)
    print(float(co2) / 100 * 1000 * 1000)
    return float(co2) / 100 * 1000 * 1000


def get_type_conso(type):
    switch = {
        0: 2.55784,
        1: 2.16185,
        2: 1.55709,
        3: 0.44436,
    }
    return switch.get(type, 0)

# print(get_common_transport(km_bus = 300, km_coach=300))

# print("\n\n")

def get_car_transport2(km, conso=5, type_conso = 0):

    url = "https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=4&h=7ed100813a406a753c01546db353190e"

    payload = '__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=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&__VIEWSTATEGENERATOR=10DAA136&rtsCalc_ClientState=%7B%22selectedIndexes%22%3A%5B%223%22%5D%2C%22logEntries%22%3A%5B%5D%2C%22scrollState%22%3A%7B%7D%7D' +\
        '&ctl05%24cdsCar%24txtMileage='+ str(km * 100) + \
        '&ctl05%24cdsCar%24ddlMileageUnit=1'+ \
        '&ctl05%24ddlCarCountry=Average'+ \
        '&ctl05%24ddlCarYear='+ \
        '&ctl05%24cefCar%24txtEfficiency='+ str(conso) + \
        '&ctl05%24cefCar%24ddlEfficiencyUnit=10'+ \
        '&ctl05%24cefCar%24ddlFuel=' + str(get_type_conso(type_conso)) + \
        '&ctl05%24btnAddCar=Calculate%2B%26%2BAdd%2BTo%2BFootprint'


    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://calculator.carbonfootprint.com',
        'Connection': 'keep-alive',
        'Referer': 'https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=4&h=1349dd890010d57a5d4b848238c3d188',
        'Cookie': 'CFp4Session=lkjefmvqwgbv1bnh3j1fxamk; CFp4CookieCheck=OK; __utma=86028682.149170279.1683794079.1683801534.1683807841.3; __utmc=86028682; __utmz=86028682.1683807841.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); CFp3TextSize=0.8em; CFpAffiliate=RADsite; __utmb=86028682.10.10.1683807841; __utmt=1; CFp4CookieCheck=OK; CFp4Session=lkjefmvqwgbv1bnh3j1fxamk',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }


    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    co2 = soup.find(["h3"], class_="nomargin").text
    print(co2)
    if co2 != None:
        co2 = co2.split("=")[1].split(" ")[1]
    print(co2)
    return float(co2) / 100 * 1000 * 1000 


def get_car_transport(km=0, hours=0, type_v=1):

    url = "https://sustainabletravel.org/wp-admin/admin-ajax.php?action=calculate_ajax&"+\
        "travel_type=vehicle"+ \
        "&vehicle_type=" + str(type_v) + \
        "&hours="+ str(hours) + \
        "&distance="+ str(km) + \
        "&calculate_unit=kilometer"+ \
        "&calculate_by=" + ("distance" if km != 0 else "hours")

    payload = {}
    headers = {
        'authority': 'sustainabletravel.org',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': '_gid=GA1.2.31493698.1683797460; ln_or=eyI0NzA4NTA4IjoiZCJ9; PHPSESSID=fe21777bd548cf5b320e92ec8387dff1; _ga_78F8JVX72C=GS1.1.1683797459.1.1.1683797879.0.0.0; _ga=GA1.2.1301583815.1683797460; _gat_gtag_UA_3096108_1=1; _gat=1; active_car=standard-car; car_values=[{"travel":"car","type":"standard-car","hours":0,"distance":20,"calculate_by":"distance","calculate_unit":"kilometer"}]',
        'referer': 'https://sustainabletravel.org/our-work/carbon-offsets/calculate-footprint/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())

    # soup = BeautifulSoup(response.text, "html.parser")
    print(response.json())
    return float(response.json()["emission"]) * 1000 * 1000




# print(get_car_transport(km = 500, type_v=2))

# print(get_car_transport2(500, conso=10, type_conso=1))

# diesel = 10 ; 2.55784
# essence = 10 ; 2.16185
# CNG = 10; 0.44436
# LPG = 10 ; 1.55709

# url = "https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=eea9acb70fc98a2e61711daa19c1c48e"

# payload = '__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=Qxo1bynXqUUBDxZ8Oo8KQFgvDyG4ZnMF%2FENj4LKqe8HEKHyHcyZxRtv417Rt8YnErTCDSmzYGVdHnd2JeOQrwMn4dbt6BT83YkYA0AUAaqGV3c32gGS%2Fs39SMbJ7ga5ctLcesaHRAm0t%2BOdQCB78yj9EyTtti0YKCNxjOkROWEYce4h72DS63XukjY3K5kFgxHm7iiatUcKetMB%2BmhI9yM4XrkBe92Mrskt5EE3hxPsD4gTbmhNPFxCwW%2FQDRkCwVVSxXuBLvarEC87Uf3j8drbinw2QEF0xAUy30CH5IaW8RMlng%2FqQroUxfnnaDULTISFQszipjOqsqwD99RJ1alC0UXRMYVyDRbQx9ZwwxNMReTCP3uaJLg2K5MCkIPPLZ9lHR%2FbQP9qY7uuGbih1dwx92Db%2FhZVd%2FpVj8M4vEydPvLk3nsEU2WFOOoZFwl2Hlk55M2t377JMFMEDgGx%2BS6pweOeK%2BVbHDooMYMzlHsXA5y0pHruzk7Z7aV0%2BfSjiEwIpTXNec747FTjVX%2BtiQujT8o1z%2FyJJnfxq5GPIZzHsPoCCyLJvqZz2EZ%2BM5nNCrHdODPh6Z3kFgLC9pCUs8cyRAzDdZzXbS2aqvgArPNMMn0Bs9Tlv12322ZbjA3RGsR9txVjFd5g2QzWNiPhwQ7QEdBfCIs4gSizEmUtu3M05ViJm7jeDSmHyKsswA5Rk%2FAFHPex9TiP6AzV6Lt2TPsccztdZx5EXeO9OBAZ%2F0HjsDORJ%2F8Ghi0xXwokrW6YDiICn4ewJhBOlbQVCUrw2gJLcBSMPWqgeD70Yw5mJPbKlWjoMGMFiyDvP4FOYvngVTJALZFT%2F3r7sZhcXS6gHnRFjreA4kP4RoAybQfEPFCBxUxDs1nBnYyw1CGDDPD%2FLynmE%2BugFoSBxanjE4Px2MJFCoLmk1xR2gDBj15tWAcDlZdyHzftJtPbRwztkrbYp%2BX7GAntu2CZWqXWgPfjGSIMQGAJnRNQh2N8TCsSnIL3g1l8gii13mfJ%2B%2FOCt8mvXH1xPEO%2FIrjIe98rKJkXQB8aXZ09VSAAuy2dfvpfZRsRXj%2Btud%2FTKElRzJInSmwT1ghWD448L4eWGztmaeikDBbuGAmCiSoIlSh6YJhErR7P92EAJNy5aIWJpi06PlwxHoM7nwQTUBacwCfaOf9D31bKdl2Gg26P1PBjnXdo9w2b%2FmKUDlwpiaTjKJZrCwUlN9v3LJ%2F7FT0KQc%2B7N6mtuX84UKOIT52M0sFjbusx9SsKpRDIYH05LL5J%2FVH9d9R0ZNwiyPXhgEaRd5IJPhYEOmZ4miGFsWiPq5gxNHeOsZvuYjEvA220FeOdQFdZFy1k61q4mcFl65dtakwF9UcnJ6s3NBQt35AfntYoP2PZPKmtCExur6Ua8zEXq69otLBSShZ%2F0qllM6AQiE6KH0NW4N%2FJgs%2Frk0MF%2FEsDXspnjRGTUSqZ5IOMo5wujZ8xhfzC%2FjfSh%2FQHSsgtKF1YL962WFcPKO4U%2ByVGJgis8%2BNp09N6cBpcyuMJf3uiZBwM0EqW3Mcvo36GH0B7V%2F6rpu77cT8ngQ2cD15ZlWWimY0xU7E%2Fj74K3%2B8vKMqIuHGAM4xOk5Ih215N3TOBbG4EOOmJOxRr4YbgsWpRBvtgFYN%2FZ6A1zyIs9XTp07UULN%2Fv%2FZZyVKI9If2JHclOBwWBrZG1%2Bfn0z9jzwM8%2B4r4RjCG079y4lN7%2FwaxTcyFL74qPQB7D9wS%2FfoU3o1Hz7bAymFwI4OoRe4s0lzVRMDarFlMH1OlhNUbqFxtsCLFqdTURsy1ALCuLTKzKGnMR8P7hucLF2%2Fdmx53GLwptuU%2BPwpBYZtG%2BbUdgWuk458%2FiN0vG7Sw3L%2B4igXPEwwMHA4GK%2By2jMJN0kv6jSkldhTId2W7rIgpAD8Z7OTflQWPglIRUq4JheY07Y6VJl8xovsH8FeITAsAMZ%2Fpezzx41UGJUn6RBLda737H95UYo9OmP%2BrkZFUmxVCm3s4xQyv9vCJluJ0wkFap0X41KT7xIA6Edy8WkkQUJ3fzNKA7dlU7R7SInlQAcEY1EVxVrqvOgNBgP%2BhKfSLPzeWSnlVa1NfATjy%2FZnZtltR0aM%2B6e37xJzqcMTNYM39VXOegWtAjOxhky9a4kIS0E4MSkfMbn2G3qb4UYsrei4CCJA5Brv7aossWtinYnVPJPnmFIP2Y5pnGSCgsfkkhZO5ZqbcFeG1KuXx97SoQieXkViIZ4cl42TB6IOE5Ht5I2YxHQ1pBxh0auKvi7KVru0XOXOjGyx79nCngRqoQGzjCKZT5J36opu%2BJIK0l4Tkul0%2FF07uH5YZgg1LlwuIqqhZv6j3ogM4KCusyLWd4jUVYT0QonTQOM40TTkz5ADvb82%2F0DQ632Behqqje56mLcwwLW%2F6ywQNAmUue7iBPbHm%2BJqCQwEH6%2FIRbc6oMTXD%2FL%2BeuAKN6iorNd%2FCa8%2FtD5FcbrVVHzFgyG3bCZ%2FWBT%2BmfF%2BxBaKTcJlMmb8d74N%2BNigCC8P94yYtIBy48P%2FzH3BwW2vg8%2Fj400trAzn02belmnbeOZR3IT9neRw%2FInybZX93KsIMmq8myMXcLNXu2EuVmCrFevWbgLfFwQGogJSENSJWLTdjs6M1t1X5oFKRHVWXHA%2BVBPNypG4K0Saldy4iNrEziDxf7I7FJMZMErO%2Ftw7mBgB%2FxB8YX45WgErdgYdpuk9DtdPCLd9oTs90b5ULOc7v4gyNMwBmJtcUVAq4%2BtoYyFyvZd32SZv%2Buz%2BL%2FhjXJcOq4N2G1Kn7EM2aOav%2F25iEI%2FDhmBYEWYel%2BwpjCb6BxKqk%2FRCfOjO0MdDiCaTlWzXAtbeSlm3RdP9Rx0l3i3I%2Fv3XMhGA%2FP8FkYGdNdGmL%2F68UL7oxN6CI1MUHrMUFv2My4ylH4UlwJ6nKRWiCbO3QIKQ8ofV82C%2BW%2BdPayU3imdAyFcNiGfpltaie4T3%2BDa6ykI%2BYNqaUCC0eh39wgZ2qQZHURYaBwGADc%2BDhB93jhmwlLGXB3nBz6Fq7DliB1iV6SwvC2QtSD2A9Dveb6IRTRTmpIQZ84G8mcQn4%2BjqEz4GO%2BooizCUKNClh3bDA9Sz8sBOxy92ccHr9v5uwSfPjUCKXVsoF86bUJszp8pCZJ1wyb2o1730GFgK%2FxSM7JT%2Ba0sd6PBjeXomaXQq4ewdkbU9pzPJMyHPRUegCwVFK%2BWqCeiaUpghc6QA1u0Vi%2FBK2p3YOriWw3Zb4f7Vy7JTt7TcJPpLXCeNXlRHX%2FnyNYq3LCezsYQkNJzSzRnFCLG0R7o0oH3RBdIMxQZ%2BdfxmIoNSuC3y9ZJHz9CUNnXitWniH9yhjcvJ9pzG06KHjzuEmHo30HI5A03pdGkMFC2cLDUBsav0ykl69N9vb45sdcGHwG9vDirUVyGI59BS6AiWG2xiZxtNGOvf9CDKqG6Kdh%2FgtQtFfr8PUgeSlCXSp40uzDzWtcTYm6uDXGuPV4ItkPG0plX5Lo3hbx64VS72KsjZQYZmdZIkvFEz6RfF%2BYpp0oh5VazJH5kdj2zDzBlBoR%2BrTQsJADXGQAHw9UYjHZeNj1Wn7YPFFZnK13S7GHf99RdFGhofVscma3LZ957ZWzYCSbkFuzPnF1iSt87bXxqmlJmuCfkTL0e%2Fq%2FwcqgVUCB%2B18QSSnKgvebNgHGejXnKKECHyVwAabnVXhw6%2FP6s5b%2BDmLPzuVgRRFiRGy%2B%2B9QBlQj70VQBVQYDfFc4NgE26nTGw7GkVSZwwyfqZG0GaLBQbrbcBj3Yxu1wGE28x4GtVUu1Iu4wXS0HPYk8HMNcGaS22e03miH1aPDt9MQCMyjwA3xDX8BlUHTOdBy8TUHG9FnH444ukbkM1k6V%2FI%2B5UJ8eJBf8zbs8KHYWLQbtUV5POM9kjdG9YRmnHuBUU5w2AsxCKkYT9aSVsZnJ3Nw6n89HAX10Ee0xdLFbvM67fyUFYbW8vgUKtCEUXEBzq2AhbwcJfPTC%2FS56e5Fvmqu51Sb8ZLup8vnD1wrbowWK08tJAcvU7TyHSlusCZCQKFXWQeu0j0PmB%2B8nENUAaR29vJetkkEucLcbEqPoyvd8dTyYuNLbtafk8nZpMz%2F6UU3u9H1DzpJNegZXAxGx1rZxeVns9%2Bjlh6T7MewnzxNL1to1iZUFhuDmPOJh4j2KFq7i4aBhz5RrH%2BU5YKe9P%2BfLVhvt%2Bf7qyzFtIZHMnITEaWxIW0fmxhfoPhk8%2Fpq3ZPAd%2BljJHEFZE0Ri1opBgkF2OXf7gxa7CqJ1MsWzhQFjQmZHYrFEsN6wE2VdHBmANyZ4YEZwDrtsawlGLC9x1MOJD7lKjJqrH2D32HqiEbvzdhyjE4twEUb7RWeHKQPuPlu5KUjaxuxyDkfE2lfB3H6GMfn2%2FYyHiR%2FNJ%2BsbdqQpgLc8BpUKz1zqf%2BuXuBlMZrtrERADvPYvu%2Bpa%2Fr1YirsmyUD4nNglnSycQ2K5EqveitfUtZdVnamgSu7VglJ3AqyuopAaUVF2vlrUKnSbfBPHtH6dZf%2BTEhOUHBdJmXeKiEgmoW9Ss7KXQczWVrFgk7C7l3hTpw4mmc1KdCsKHnkxG0UX2DFizJkw1YZqBPZbMZH%2B3oScVfVg1cmiyUiELlP3Mm%2F0RXbjrFmTJfdnzHR7LTOO3EK0tEJG4b6UngZ5QZyucuI0JNWC%2FMi%2BQ3pQl7H28nEZhH3YqvTS2qHy2qh1AzC%2B7XRyxgkOgPpvZTZ2WnackH%2BfCoEAL4YVkSE0ljh6ZYdDubd33E7p0YOBa%2FxnXkqRFj7anTIr3Ayas%2B1fcKuaxD8Jj29lZsC48sy97kKm48cjgGKa3lUed1Ag8Fg3kZYUBV9hIYQZr50wRs7WcRY0SKq1OAnH75LaBnaB%2FyPtJPPq3hYYE8b9B2TF41gzpXCTgGJA08oXPdBoYkerY5hHojYGDPyD7OPCXpSqoGAJgTlbXUQm4dFM77vGSiL4PrKh4nFDIraXmXp0PsCP1MlO0Nfs8OT%2FHCrca26qqbsVYWsMjZl6xQhIEPK%2BP%2B98vlVsXqHQ5NRxTO9tLM50fMaCJGmezIhOQIwC0cOdTtIjvxDRIFEbx4ga3Oa7hSc2qwE7AfdlFRwnA2G3FbhNGzOfIkb%2B%2B79S2E0cSyCuJxF1ReQn5svPHWn3KulY9Es4A1mB15HiuXWpNU4GgXGexLXAPrm4Z6dvNnMf5B3vlubDLB4lPwuXj85eyJphImraoh58xsYBIJa16NjuqJTid1cAVy6uRAEK3o0EMwY0Jizxm%2FLBCM1LWU7YLZUJYCizVUCgTOhEVIr%2FfGDsK%2Fb71W3Zl0HafVuItG9IR2PAAJdEjajUmcGttKyIuYgPyAbpDtPiTwv%2BO3ove8Cyl9hAuasssPbZdjFXXNQYeqtZCQl6q50cTZro6EL9BMatSgVAbGd1BdGrUMoGXYUJJuKtlHGaS41HTly4uoHEkuj4WCQ460qVVJziHeXdCuNMQmnSAoB5ppJbv4QDX1Z%2BTgMJfKg4Ximd7zGboeg%2Fb81%2FxQfg97Xr%2BzzoRtU6CbUINObJSFEcIm1wFRptqGzMHl9nxWhXLfbLFZtINQ%2B29Nd5xehUjf7YOgktsVGMTv1QbXNYOFe%2BKmSmBQ6ummK1QVjuLrR54cKr%2BQP7xjM1UaNs6UnpkxvtMyDToo8WxJFYB6svYaErIcT9zMvPaOX0EcoL%2BEj4SPZ3hCOa%2FLrDDojit%2BHRITpZP5omjPCG%2F4Z%2FBqFxWmA9Gcsuoo%2BqkwbEuf0eZimiiZExde%2FXOJl6OrlyBoC5snHNAG%2B7P6J0Z9U0nOuXA%2FhrQMqRq2Es3gDDWFN0MqWVzmrNUtofuX4vAK4nlWnZ%2FhtM5bMY1VqsJHjB7qYnbLKhPITfJoXXXlCtv1OGtNui%2FHb8Y%2BwRIkcYAd%2BDu%2F7%2BSoOh9QkUhkroiJpO6dkHwzkd6wxtmNMFE3%2By49cOF3vw78fvwzYjkstxueLbugDnH19vWw%2FkjKJ125APptb%2BgVEXPBQlGSFSHQdJLHHJ2Fx3TSWIFS8I4QSXr2slgPj04LLtnMjFYvVcID7axjPc01hP1vYu%2ByTIoArnrWiRt83tPnGJ4vbQ%2Fe7M1s7qi%2FkfNLGE%2Fsicn9XwGfkw4X53voeWBY31BBS78%2BdYkVcQJxo2HkBmo8UYT1HX5229iVU9lcfJcwnXNlfVUNIdjFCP%2BhVKPQYHhZ%2BhuYO%2FEcqOCOb%2BlWR1koZcL25rIJOLJqV0VhIIBuBPJtQcfXkC4YvItwk%2Bu3hXXikWmkb2RUk1B7ws1r%2FznrshWASP9gmZgZw6hwgWvBSQ0egytpgWyAxmbuMZShIXFet8IOw4yZXB4byJSLfMjhqwXbFL%2Fl8Rr9ms3wQijMYuiOGgjQuab39tR2G7ho8AVn1MAPteLFxqu%2BOqo6c38GYUZADKjV4%2BzBYwlo9%2FqaSB6gRDkZHsjdQi2amzMWhzHzib4w4aCLnjICyKK5gHx86PGKMIzl%2FtzYG8jX7HXN%2B6Gps2skaMjIe30uGz4EqMzTbW6X8pbcPZ4y5FDgEfxCkxKONxpJAFaQa6ZcSOBg2IV5k9EcQ2pr%2B5v8qj1spg85eYf7acZrPiM9Jo2iJmso%2FbExt56&__VIEWSTATEGENERATOR=10DAA136&rtsCalc_ClientState=%7B%22selectedIndexes%22%3A%5B%225%22%5D%2C%22logEntries%22%3A%5B%5D%2C%22scrollState%22%3A%7B%7D%7D&ctl05%24cdsBus%24txtMileage=500&ctl05%24cdsBus%24ddlMileageUnit=1&ctl05%24cdsCoach%24txtMileage=&ctl05%24cdsCoach%24ddlMileageUnit=1&ctl05%24cdsNatRail%24txtMileage=&ctl05%24cdsNatRail%24ddlMileageUnit=1&ctl05%24cdsIntRail%24txtMileage=&ctl05%24cdsIntRail%24ddlMileageUnit=1&ctl05%24cdsTram%24txtMileage=&ctl05%24cdsTram%24ddlMileageUnit=1&ctl05%24cdsTube%24txtMileage=&ctl05%24cdsTube%24ddlMileageUnit=1&ctl05%24cdsTaxi%24txtMileage=2500&ctl05%24cdsTaxi%24ddlMileageUnit=1&ctl05%24btnAddBus=Calculate%2BBus%2B%26%2BRail%2BFootprint'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-GB,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://calculator.carbonfootprint.com',
#     'Connection': 'keep-alive',
#     'Referer': 'https://calculator.carbonfootprint.com/calculator.aspx?c=Full&tab=6&h=eea9acb70fc98a2e61711daa19c1c48e',
#     'Cookie': 'CFp4Session=uc3cn1hro3bpq2jqxzg41dhk; CFp4CookieCheck=OK; CFp3TextSize=0.8em; CFp4CookieCheck=OK; CFp4Session=uc3cn1hro3bpq2jqxzg41dhk; CFpAffiliate=RADsite',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'iframe',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
#     'TE': 'trailers'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# soup = BeautifulSoup(response.text, "html.parser")
# co2 = soup.find(["h3"], class_="nomargin").text
# print(co2)
# if co2 != None:
#     co2 = co2.split("=")[1].split(" ")[1]
# print(co2)
# print(float(co2) / 100 * 1000 * 1000)
