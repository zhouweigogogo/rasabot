from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.actions.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.types import DomainDict


# Q1： 如果在填写表单的过程中，输入错误，是否可以更改输入值
# Q2： 如果在填写完成之后，是否可以返回上文更改错误值


# 可以写成自定义也可以不写，主要是方便调试
class ActionGoodbye(Action):
    def name(self) -> Text:
        return 'action_goodbye'

    def __init__(self):
        super().__init__()

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        print('\n ActionGoodbye-------------')
        currentSlots = tracker.current_slot_values()
        for slot in currentSlots:
            print('run slot:\t\t%s=%s' % (slot, currentSlots[slot]))

        dispatcher.utter_message(response="utter_goodbye", **tracker.slots)

        print('Restarted()')
        return [Restarted()]


# 提交表单
class ActionPigForm(Action):
    def name(self) -> Text:
        return "action_diagnose_form_submit"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict]:
        dispatcher.utter_message(response='utter_ask_confirm', **tracker.slots)
        return []


class TicketFormAction(FormAction):
    def name(self) -> Text:
        return "pig_form"

    def required_slots(self, tracker: Tracker) -> List[Text]:
        return ["tiwen", "pifu", "maose", "huxi", "paixie", "fenbian", "jingshen"]

    def extract_other_slots(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if not slot_to_fill:
            return super().extract_other_slots(dispatcher, tracker, domain)
        else:
            return {}

    # def slot_mappings(self):
    #     return {
    #         "city_depart": [
    #             self.from_entity(entity="city", intent="info_city")
    #         ],
    #         "city_arrive": [
    #             self.from_entity(entity="city", intent="info_city")
    #         ],
    #     }


# 主要查询函数
class ActionDiagnosePig(Action):

    def name(self) -> Text:
        return "action_diagnose_pig"

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entitys = {'tiwen': {'体温升高': '1', '体温降低': '2', '体温正常': '3'},
                   'pifu': {'皮肤正常': '1', '皮肤潮红': '2', '皮肤红肿': '3', '皮肤暗沉': '4', '皮肤有红斑': '5', '皮肤有紫斑': '6', '皮肤发白': '7',
                            '皮肤出血': '8'},
                   'maose': {'毛色正常': '1', '毛色暗沉': '2', '毛色鲜亮': '3'},
                   'huxi': {'呼吸急促': '1', '呼吸正常': '2', '呼吸较慢': '3'},
                   'paixie': {'便秘': '1', '腹泻': '2', '正常': '3'},
                   'fenbian': {'粪便较稀': '1', '粪便正常': '2', '粪便较硬': '3'},
                   'jingshen': {'精神亢奋': '1', '精神低沉': '2', '精神正常': '3'}}

        currentSlots = tracker.current_slot_values()
        ask_str = ""
        for slot in currentSlots:
            if slot in entitys:
                ask_str += entitys[slot][currentSlots[slot]]
        print(ask_str)
        import json
        with open("diseases_pig.json", "r", encoding="utf-8") as fp:
            data = json.load(fp)
            if ask_str in data:
                disease = data[ask_str]
                print("疾病名：", disease["name"])
                print("疾病症状：", disease["symptom"])
                print("救治措施：", disease["treat"])
                dispatcher.utter_message("疾病名：" + disease["name"])
                dispatcher.utter_message("疾病症状：" + disease["symptom"])
                dispatcher.utter_message("救治措施：" + disease["treat"])

                api_succeed = True
            else:
                print("抱歉，未查询到此病")
                api_succeed = False

        return [SlotSet("api_succeed", api_succeed)]


class ActionAskConfirm(Action):
    def name(self) -> Text:
        return "action_ask_confirm"

    def __init__(self):
        super().__init__()

    def run(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        slots = []
        currentSlots = tracker.current_slot_values()
        for slot in currentSlots:
            print('run slot:\t\t%s=%s' % (slot, currentSlots[slot]))
            slots.append(currentSlots[slot])
        response = "请您核对患猪的特征：\n体温状况：\t\t{}\n皮肤状况：\t\t{}\n毛色状况：\t\t{}\n呼吸状况：\t\t{}\n排泄状况：\t\t{}\n粪便状况：\t\t{}\n精神状况：\t\t{}".format(
            *slots[1:])
        print(response)
        dispatcher.utter_message(text=response)
        dispatcher.utter_message(
            image="https://s2.loli.net/2022/09/06/LjXiC69lOcWna4R.jpg")
        dispatcher.utter_message(buttons=[
            {"payload": "/affirm", "title": "是"},
            {"payload": "/deny", "title": "否"},
        ])
        return []


class ActionAskConfirmThenNo(Action):
    def name(self) -> Text:
        return 'action_ask_confirm_then_no'

    def __init__(self):
        super().__init__()

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        print('\n ActionAskConfirmThenNo-------------')
        currentSlots = tracker.current_slot_values()
        # 第二次调用可能为空
        for slot in currentSlots:
            print('run slot:\t\t%s=%s' % (slot, currentSlots[slot]))

        dispatcher.utter_message(response="utter_ask_confirm_then_no", **tracker.slots)
        print('Restarted()')
        return [Restarted()]


class ActionApiSucceedTrue(Action):
    def name(self) -> Text:
        return 'action_api_succeed_true'

    def __init__(self):
        super().__init__()

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        print('\n ActionApiSucceedTrue-------------')
        currentSlots = tracker.current_slot_values()
        for slot in currentSlots:
            print('run slot:\t\t%s=%s' % (slot, currentSlots[slot]))

        dispatcher.utter_message(response="utter_api_succeed_true", **tracker.slots)

        print('Restarted()')
        return [Restarted()]


class ActionApiSucceedFalse(Action):
    def name(self) -> Text:
        return 'action_api_succeed_false'

    def __init__(self):
        super().__init__()

    def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> List[Dict[Text, Any]]:
        print('\n ActionApiSucceedFalse-------------')
        currentSlots = tracker.current_slot_values()
        for slot in currentSlots:
            print('run slot:\t\t%s=%s' % (slot, currentSlots[slot]))

        dispatcher.utter_message(response="utter_api_succeed_false", **tracker.slots)
        print('Restarted()')
        return [Restarted()]


class ActionRestartConversation(Action):
    def name(self) -> Text:
        return "action_restart_conversation"

    def __init__(self):
        super().__init__()

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict]:
        print('\n ActionRestartConversation-------------')
        currentSlots = tracker.current_slot_values()
        # 返回一个字典{slot:value}
        for slot in currentSlots:
            print("run slot:\t\t%s=%s" % (slot, currentSlots[slot]))

        print('Restarted()')
        return [Restarted()]


# class ActionAskSlotThenChange(Action):
#     def name(self) -> Text:
#         return "ask_slot_then_change"
#
#     def __init__(self):
#         super().__init__()
#
#     def run(
#             self,
#             dispatcher: "CollectingDispatcher",
#             tracker: Tracker,
#             domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:

