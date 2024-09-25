import requests
import pandas as pd
import time

# URL to get the general data about all players
bootstrap_static_url = "https://fantasy.premierleague.com/api/bootstrap-static/"

# URL pattern to get the weekly summary data for a player by their element ID
element_summary_url = "https://fantasy.premierleague.com/api/element-summary/{}/"

# Dictionary to map element_type to player position
position_mapping = {
    1: 'Goalkeeper',
    2: 'Defender',
    3: 'Midfielder',
    4: 'Forward'
}

# Function to get the list of all players and their IDs
def get_all_players():
    response = requests.get(bootstrap_static_url)
    data = response.json()
    players = data['elements']
    return players

# Function to get weekly data for a specific player by their element ID
def get_player_weekly_data(player_id):
    response = requests.get(element_summary_url.format(player_id))
    return response.json()

# Main function to extract data for all players
def extract_all_players_data():
    players = get_all_players()  # Get the list of all players
    all_player_history = []

    # Loop through each player
    for player in players:
        player_id = player['id']
        print(f"Fetching data for player ID: {player_id}")

        # Get player weekly data
        player_weekly_data = get_player_weekly_data(player_id)

        # Get the player's position based on element_type
        player_position = position_mapping.get(player['element_type'], 'Unknown')

        # Loop through each gameweek history and create separate rows
        for gameweek in player_weekly_data.get('history', []):
            player_data = {
                'id': player['id'],
                'first_name': player['first_name'],
                'second_name': player['second_name'],
                'team': player['team'],
                'position': player_position,  # Map element_type to position
                'fixture': gameweek['fixture'],
                'opponent_team': gameweek['opponent_team'],
                'total_points': gameweek['total_points'],
                'was_home': gameweek['was_home'],
                'kickoff_time': gameweek['kickoff_time'],
                'team_h_score': gameweek['team_h_score'],
                'team_a_score': gameweek['team_a_score'],
                'round': gameweek['round'],
                'minutes': gameweek['minutes'],
                'goals_scored': gameweek['goals_scored'],
                'assists': gameweek['assists'],
                'clean_sheets': gameweek['clean_sheets'],
                'goals_conceded': gameweek['goals_conceded'],
                'own_goals': gameweek['own_goals'],
                'penalties_saved': gameweek['penalties_saved'],
                'penalties_missed': gameweek['penalties_missed'],
                'yellow_cards': gameweek['yellow_cards'],
                'red_cards': gameweek['red_cards'],
                'saves': gameweek['saves'],
                'bonus': gameweek['bonus'],
                'bps': gameweek['bps'],
                'influence': gameweek['influence'],
                'creativity': gameweek['creativity'],
                'threat': gameweek['threat'],
                'ict_index': gameweek['ict_index'],
                'starts': gameweek['starts'],
                'expected_goals': gameweek['expected_goals'],
                'expected_assists': gameweek['expected_assists'],
                'expected_goal_involvements': gameweek['expected_goal_involvements'],
                'expected_goals_conceded': gameweek['expected_goals_conceded'],
                'value': gameweek['value'],
                'transfers_balance': gameweek['transfers_balance'],
                'selected': gameweek['selected'],
                'transfers_in': gameweek['transfers_in'],
                'transfers_out': gameweek['transfers_out']
            }
            all_player_history.append(player_data)

        # Pause between requests to avoid rate-limiting
        time.sleep(1)  # Adjust sleep time if necessary

    return all_player_history

# Extract data and save it to a pandas DataFrame for analysis
def save_data_to_dataframe():
    data = extract_all_players_data()
    df = pd.DataFrame(data)
    return df

# Run the extraction
if __name__ == "__main__":
    df = save_data_to_dataframe()
    df.to_csv('fpl_players_gameweek_data.csv', index=False)  # Save the data to a CSV file
    print("Data extraction completed and saved to fpl_players_gameweek_data.csv")
