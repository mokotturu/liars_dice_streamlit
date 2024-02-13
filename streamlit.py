from streamlit_card import card
from streamlit_extras.grid import grid

import streamlit as st


def dice_number_to_word(number):
	match number:
		case 1:
			return "one"
		case 2:
			return "two"
		case 3:
			return "three"
		case 4:
			return "four"
		case 5:
			return "five"
		case 6:
			return "six"
		case _:
			return "unknown"

if __name__ == '__main__':
	st.set_page_config(
		page_title="Liar's Dice Game",
		page_icon="🎲",
		layout="wide",
		initial_sidebar_state="auto"
	)

	# heading and current turn
	heading = st.title("Liar's Dice Game", anchor=False)
	st.divider()
	current_turn_container = st.empty()
	current_turn = current_turn_container.info(f"Current Turn: Confederate 1")

	# draw confederates and the robot
	external_players = st.columns(3)
	external_player_titles = [
		"Confederate 1",
		"Confederate 2",
		"Robot"
	]
	for player_idx, player_col in enumerate(external_players):
		tile = player_col.container(border=True)
		tile.header(external_player_titles[player_idx], anchor=False, divider="gray")
		tile.text(f"Dice hidden")

	# draw the player
	participant_dice_data = [6, 5, 4, 3, 2, 1]
	participant_container = st.container(border=True)
	participant_container.header("You", anchor=False, divider="gray")
	participant_view = participant_container.columns([0.4, 0.6])

	# left column
	participant_view[0].button("Roll Dice", type="primary", disabled=True)
	participant_view[0].markdown("#### Your dice:")

	# hack to make the columns smaller
	pseudo_width = 0.7
	col_spec = [pseudo_width / len(participant_dice_data) for _ in participant_dice_data]
	col_spec.append(1 - sum(col_spec))
	cols_wrapper = participant_view[0].empty()
	cols = cols_wrapper.columns(col_spec)
	for idx, col in enumerate(cols):
		if idx == len(cols) - 1:
			break
		col.image(f"./assets/dice_{dice_number_to_word(participant_dice_data[idx])}.svg", width=50, use_column_width="never")

	# right column
	participant_view[1].markdown("#### Your bid:")
	bid_container = participant_view[1].columns(6)
	for die_idx, bid_col in enumerate(bid_container):
		for i in range(6):
			bid_col.button(f"{dice_number_to_word(i + 1)} {die_idx + 1}s", type="primary", use_container_width=True, disabled=True)

	# draw the message box
	message_container = st.container(border=True)
	message_container.header("Messages from the robot", anchor=False, divider="gray")
	message_container.chat_message("assistant").write(f"Challenge the last bid!")