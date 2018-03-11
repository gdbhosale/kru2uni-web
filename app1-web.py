import web
import krutidev2unicode as ku

urls = (
    '/(.*)', 'kru2uni'
)
app = web.application(urls, globals())

class kru2uni:
    def POST(self, name):
        i = web.input()
        print i
        data = i.data
        return ku.kru2uni(data)

if __name__ == "__main__":
    app.run()