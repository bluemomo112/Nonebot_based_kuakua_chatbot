from nonebot import on_command,CommandSession
import nonebot
import requests,json


@on_command('say', aliases=('每日一句'))
async def everydaysay(session:CommandSession):
    says=session.state.get('says')
    url = 'http://open.iciba.com/dsapi/'
    res =requests.get(url)
    data= res.json()
    content_e = data['content']
    content_c =data['note']
    # img_url =data['fenxiang_img']
    await session.send(content_e)
    await session.send(content_c)
    # await session.send(f'[CQ:image,file={img_url}]')  #只有酷Qpro 才能发送图片
