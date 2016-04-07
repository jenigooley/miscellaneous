
def url_split(xxx):
    url_lst = []
    #if xxx.count("/") >= 3:
    def path(xxx):
        return "path:" + xxx.split("/",3)[3]

    def protocol(xxx):
        return "protocol:" + xxx.split(":")[0]

    def domain_name(xxx):
        return "domain name:" + xxx.split("//")[-1].split("/")[0]

    url_lst.append(domain_name(xxx))

    if len(xxx.split("w",-1)) > 0:
        url_lst.append(protocol(xxx))

    if xxx.count("/") >= 3:
        url_lst.append(path(xxx))

    return "  ".join(url_lst)

print url_split("http://www.heywnow.ie/one/two/three/four/five/six")
