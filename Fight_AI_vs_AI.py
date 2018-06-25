
import argparse

from Reversi import Reversi
from dqn_agent import DQNAgent


if __name__ == "__main__":
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path")
    parser.add_argument("-s", "--save", dest="save", action="store_true")
    parser.set_defaults(save=False)
    args = parser.parse_args()

    # environmet, agent
    env = Reversi()
    agent1 = DQNAgent(env.enable_actions, env.name, env.screen_n_rows, env.screen_n_cols)
    agent1.load_model("models1/Reversi.ckpt")

    agent2 = DQNAgent(env.enable_actions, env.name, env.screen_n_rows, env.screen_n_cols)
    agent2.load_model("models2/Reversi.ckpt")


    # game
    print("------------- GAME START ---------------")
    while not env.isEnd():
        # print("*** userターン○ ***")
        # env.print_screen()
        # enables = env.get_enables(1)
        # if len(enables) > 0:
        #     flg = False
        #     while not flg:
        #         print("番号を入力してください")
        #         print(enables)
        #         inp = input('>>>  ')
        #         action_t = int(inp)
        #         for i in enables:                
        #             if action_t == i:
        #                 flg = True                       
        #                 break
                
        #     env.update(action_t, 1)
        # else:
        #     print("パス")
            
            
        #if env.isEnd() == True:break
        
        print("*** AI1ターン●  ***")
        env.print_screen()
        enables = env.get_enables(1)
        if len(enables) > 0:
            qvalue, action_t = agent1.select_enable_action(env.screen, enables)
            print('>>>  {:}'.format(action_t))              
            env.update(action_t, 1)
        else:
            print("パス")

        key = input("Next")
 
        print("*** AI2ターン○ ***")
        env.print_screen()
        enables = env.get_enables(2)
        if len(enables) > 0:
            qvalue, action_t = agent2.select_enable_action(env.screen, enables)
            print('>>>  {:}'.format(action_t))              
            env.update(action_t, 2)
        else:
            print("パス")

        ket = input("Next")

    print("*** ゲーム終了 ***")
    if env.winner() == 1:
        print("AI1の勝ち！ AI1スコアは、{:}です。".format(env.get_score(1)))
    else:
        print("AI2の勝ち！ AI2のスコアは、{:}です。".format(env.get_score(2)))
    
