import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
from PyQt6.uic import loadUi
from Package import streaming_asr_demo
from Package import http_method as htp
import re
import markdown

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("untitled.ui", self)  # 直接加载 .ui 文件
       
    def addControl(self,str_message):
        self.text_control.appendPlainText(str_message)

    def on_btn_start_clicked(self):
         # 弹出文件选择对话框
        file_path, _ = QFileDialog.getOpenFileName(
            self,  # 父窗口
            "选择音频文件",  # 对话框标题
            "",  # 初始目录（空字符串表示当前目录）
            "音频文件 (*.wav)"  # 文件过滤器
        )
        
        if(file_path == "") :
            self.addControl("没有正确找到文件路径")
            return
        
        ret = streaming_asr_demo.test_one(file_path)
        print(ret)
        text = ret['result']['payload_msg']['result'][0]['text']
        #text = '今天是2025年1月13日，星期一，农历腊月十四。欢迎收看今天的资讯早班车，让我们大家一起来关注一下过去24小时的重要资讯。 多地辟谣离婚信号传闻据顶端新闻报道，近日，网络上流传着一则关于离婚信号的消息。消息称，青岛、广州、大连、西安、南京等多个城市的婚姻登记处对离婚业务进行了数量限制。 引发了广泛关注和讨论，有网友甚至戏称这年头离婚都要靠抢号了。对此，有记者联系了上述城市的多个婚姻登记处，工作人员均明确表示不存在离婚信号，并称婚姻登记处大都采取网上预约和现场排队相结合的方式。 一般优先办理线上预约的离婚申请。而在本月烧早前，湖北京市的经事直播栏目也针对离婚信号传闻，联系了广州、大连、西安的多个婚姻登记处进行核实。 其中， 广州越秀区婚姻登记处的工作人员明确表示，并没有所谓的离婚信号政策，但由于办理离婚登记需要大约40分钟的时间，且婚姻登记处每天的业务量是有限的，因此并不是全天都能办理离婚登记。 当记者询问一天可以预约多少个名额时，工作人员表示，预约人数由系统决定，他们并不清楚具体数字。大连市甘井子区婚姻登记处的工作人员也表示，并没有离婚限号的政策，只是要预约，但现在离婚的人太多。 2月7日之前都没有号了。至于一天有多少网上预约名额，工作人员表示并不清楚。据了解，近几十年来，国内的离婚率一直在不断走高而。 数据显示，1978年我国的离婚率仅为千分之零点二，而到了40年后的2019年，离婚率已经飙升到了千分之三点四，40年的时间增长了近20倍。 2020年后，由于新官疫情和离婚冷静期规定的实施，离婚率出现了短暂的下降。不过， 伴随着疫情防控结束，近两年的离婚率又迅速出现了反弹。不。 电影票房一招退回十年前国家电影局近日公布的数据显示，2024年国内电影总票房为425.02亿元，较2023年的549.21亿元大幅下滑了22.6%，甚至比2015年的437.73亿元还少了12.7亿元。 直接退回到了10年前的水平。 其中，占比78.68%的国产影片票房为334.39亿元，较2023年的460.05亿元下滑了27.3%。 与此同时，城市院线观影总人次仅剩下10.1亿，也大幅低于2023年的12.99亿。具体来看，去年一年的票房走势可谓是高开低走。 在去年的三大黄金档期中，只有年初的春节档表现强劲，票房突破80亿元，创下历史新高。 但在年终的暑期档和年末的国庆档却都出现了大幅下滑，其中暑期档票房仅为116亿元，相较于2023年的206亿几乎腰斩。 至于人们为什么都不爱去电影院看电影啊？第一财经曾在报道中引述制片人陈彩云的话说，当前的经济环境下，电影并不是刚性需求，文化消费都放在了第二位。 有不少网友就认为，看电影的成本普遍高于其他娱乐活动，与其花三五十元去电影院看一部， 可能让人失望的电影，还不如等一等之后在流媒体平台上观看。还有不少网民透露，过去一年自己基本都是在视频平台看小帅小美们的电影解说。 对于这种现象，国内知名导演张艺谋此前曾在接受采访时直言很无语，并强烈呼吁大家重返电影院，还称电影院的氛围是独一无二的往事。 尽管有业内大佬呼吁，但这也没能改变电影院正在逐渐被观众抛弃的现实。中国电影家协会发布的2024中国， 电影观众变化趋势报告就显示，2024年观众通过线上刷短视频的频率持续上升，而去影院看电影的频率增速下降了9%。 伴随着票房收入的下滑，影视公司的经营业绩也出现了大面积亏损。统计数据显示，2024年第三季度，在 a 股上市的10家主要电影公司中，有7家公司出现了亏损，还有多家公司由于连续多年亏损导致财务指标不达标，将在2025年面临巨大的退市压力。 此外，由于行业整体不景气，去年11月，横店影视城还传出了群众演员集体匠心的消息。对此，有分析指出，短视频行业的大发展极大地改变了用户的娱乐习惯。 整个影视行业都在逐步去中心化，如今电影院早已不是呈现影视作品的唯一场所，影视公司也不再是影视作品创作的唯一中心。 若传统电影行业不能主动求变，适应短视频时代用户变化的需求，那么整个行业都必将被用户所。 所抛弃，并逐渐消失在时代的浪潮之中。 香港电影业陷入寒冬，票房创13年新低。据港媒报道，香港电影票房有限公司今日公布的最新数据显示，排除不能做直接比较的疫情期间，2024年香港电影业票房收入仅为13.4亿港元，直接倒退回了2011年的水平。 此外，香港电影工作者总会发言人田启文近日还在一， 当电台节目上透露香港去年共有9家戏院结业，早已反映全年票房收入创新低的现实，一切已在意料之中。他还预计，香港电影票房收入下滑的情况，难以在短期内逆转。 开展跟着电影频美食活动近日，国家电影局联通商务部发布了关于开展跟着电影皮美食活动的通知。通知提出，鼓励电影企业加强对餐饮文化内涵的挖掘展示。 推出更多表现美食文化主题的电影作品，鼓励电影企业、餐饮企业、商业综合体以及互联网平台企业等联合开展电影加美食促销费活动，推动更多观影人流和餐饮客流相互转化。 鼓励电影院创新影院空间布局，探索发展电影院加餐饮融合业态，拓展看电影、品美食消费场景。通知最后还写到，要组织动员本地电影企业、餐饮企业、互联网平台企业、商业银行等积极参与，并加强对好精， 经验、好做法的总结、提炼、复制、推广，营造良好消费氛围经验。 加州山火蔓延，大量房屋被烧。综合外媒报道，当地时间1月7日以来，美国加利福尼亚州洛杉矶野火疯狂研烧，截至1月12日，山火已造成24人死亡，1万多栋建筑物被破坏或烧毁，18万人被迫撤离。 其中洛杉矶县沿海高档住宅区帕利塞兹的灾情最严重。 许多人眼睁睁地看着他们的房屋被烧成灰烬。有当地居民表示，他对地方官员感到彻底失望。还有居民称，地方当局对普通百姓弃之不管，任由他们的家园被火烧。 据悉，因消防员不足，救火工作被拖慢。洛杉基县消防部门负责人说，洛杉矶区域内各机构约有9,000名消防员，不足以同时应对多场大规模山火。 与此同时，由于趁火打劫和盗窃案件频发，洛杉矶警方还在， 在灾民疏散区颁布了萧禁令，围立者将面对监禁或罚款处分。有预测机构估计，这次野火灾害造成的经济损失可能高达1,500亿美元，灾后重建工作会异常艰巨，房主的保险成本也将飙升。 对此，美国总统拜登表示，这是加州历史上最严重的火灾，联邦政府将全额承担180天的救灾费用。美国当选总统特朗普则在社交媒体发文，猛烈批评了加州州长纽森应对灾情不利。呼。 扭森辞职，并称这次火灾显示出拜登和纽森组合的严重无能和糟糕管理，呼吁扭。 接下来是今天的联播简讯。 1月12日，国家卫健委召开新闻发布会，相关负责人在会上介绍，我国近期处于流感相对高发期，单位超过去年流行记的水平。 全国发热门诊、急诊患者数量呈现一定程度的上升趋势，但总体低于去年同期水平。未出。 县医疗资源明显紧张的情况。与此同时，中国疾控中心研究员王丽萍还在会上表示，当前仍将呈现多种呼吸道传染病交替或叠加流行态势，但军事已知病原体，未出现新发传染病建议。 据央视新闻报道，近日，全国多地医院接诊的肉毒素中毒患者明显增多。据了解，不少患者为了快速瘦身除皱，注射了来路不明的肉毒素，虽然短时间内获得了不错的美容塑身效果。 但却造成了健康困扰，严重的甚至危及生命。有记者调查后发现，部分美容机构使用的肉毒素都来自地下非法加工，每支成本仅1.5元，出厂价20元，最终卖给消费者的价格都高达千元左右。 近期，咖啡豆期货价格飙升，近一年累计涨幅超过了70%，远超同期黄金涨幅，并创出了近50年来的新高。据悉，2024年，由于长期的极端干旱天气，全球， 咖啡的主产地巴西和越南都出现了产量锐减，导致供需失衡。有国际咖啡贸易商预测，2025至2026年度，全球咖啡豆产量将出现850万袋的短缺。 供应偏紧或将导致价格长期维持在高位。 以上就是本期资讯早班车的全部内容，如果您觉得本视频对您有帮助，麻烦您点个赞，欢迎关注我们资讯早班车是。 你每天刷牙洗脸的好伙伴！我们每天早晨不见不散！你每天。'
        self.text_raw_texture.appendPlainText(text)

        api_key = "24d25586-dd58-46ff-adfa-1a3867f599ba"  # 替换为你的API密钥
        model = "ep-20250120114002-t7pgg"  # 替换为你的模型名称
        


        str_simplify = "请你使用MarkDown形式，将我接下来说的话输出为一个摘要 ：" + text

        messages = [
        {"role": "system", "content": str_simplify},
        ]
        
        ret_simplify = htp.send_chat_request(api_key,model,messages)
        self.text_simplify_texture.appendPlainText(ret_simplify)

        str_mindmap = "请你使用MarkDown的形式，将我接下来的话使用MarkMap的格式转换成一个思维导图，并且发还给我：" + text
        messages = [
        {"role": "system", "content": str_mindmap},
        ]
        ret_mindmap = htp.send_chat_request(api_key,model,messages)

        self.text_mindmap.appendPlainText(ret_mindmap)

        
        self.addControl("分析完毕！")

        #将Markdown摘要保存
        html = markdown.markdown(ret_simplify)
        with open("simplify.html", "w", encoding="utf-8") as f:
            f.write(html)

        #将mindmap输出为思维导图
        save_markdown_to_html(ret_mindmap,"ret.html")


def save_markdown_to_html(markdown_text, output_file="output.html"):
    # HTML模板
    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Markmap</title>
        <style>
          svg.markmap {{
            width: 100%;
            height: 100vh;
          }}
        </style>
        <script src="https://cdn.jsdelivr.net/npm/markmap-autoloader@0.16"></script>
      </head>
      <body>
        <div class="markmap">
          <script type="text/template">
            {markdown_content}
          </script>
        </div>
      </body>
    </html>
    '''

    # 将Markdown文本插入到HTML模板中
    html_content = html_template.format(markdown_content=markdown_text)

    # 保存生成的HTML文件
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"HTML文件已保存到 {output_file}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())