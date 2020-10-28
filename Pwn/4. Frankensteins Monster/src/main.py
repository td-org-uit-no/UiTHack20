from flask import Flask, render_template, request
import dill

app = Flask(__name__)

flag = "UiTHack20{p1ckeled_brAiNs_Are_his_favouriTe}"


@app.route('/', methods=['POST', 'GET'])
def index():
    print(request)
    if request.method == 'POST':
        request.get_data()
        s = request.data
        inp = extract_input(s)
        unpickle_result = unpickle_string(inp)
        if unpickle_result == '':
            unpickle_result += 'function did not return a result'
        app.logger.info(f'res: { unpickle_result}')
        return render_template('index.html', unpickle_result=unpickle_result)

    return render_template('index.html')


def extract_input(bstring):
    rawstring = bstring.decode('unicode-escape')
    if rawstring.startswith("input=b'"):
        body = rawstring[len("input=b'"):-3]
        return body.encode('ISO-8859-1')
    elif rawstring.startswith("input="):
        body = rawstring[len("input="):-2]
        return body.encode('ISO-8859-1')
    else:
        return bstring


def unpickle_string(s):
    try:
        print('input:', s)
        o = dill.loads(s)
        print('unpickled to:', o)
        if o:
            try:
                print(o)
                res = o()
                print(res)
                if res:
                    return res
            except:
                return 'failed to run function'
    except:
        return f'dill failed to unpickle string {s}'


if __name__ == '__main__':
    app.run(debug=True)
