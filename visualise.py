import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the saved data
df = pd.read_csv('fpl_players_gameweek_data.csv')

# Example 1: Top 10 Players by Total Points
def plot_top_players_by_points():
    top_players = df.groupby(['first_name', 'second_name']).sum()['total_points'].nlargest(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='total_points', y='second_name', data=top_players, palette='viridis')
    plt.title('Top 10 Players by Total Points')
    plt.xlabel('Total Points')
    plt.ylabel('Player Name')
    plt.show()

# Example 2: Scatter Plot of Goals Scored vs Assists
def plot_goals_vs_assists():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='goals_scored', y='assists', hue='position', data=df, palette='Set1', s=100)
    plt.title('Goals Scored vs Assists by Player Position')
    plt.xlabel('Goals Scored')
    plt.ylabel('Assists')
    plt.show()

# Example 3: Line Plot of Player Value Over Time (for a specific player)
def plot_player_value_over_time(first_name, second_name):
    player_data = df[(df['first_name'] == first_name) & (df['second_name'] == second_name)]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='event', y='value', data=player_data, marker='o', color='blue')
    plt.title(f'Player Value Over Time - {first_name} {second_name}')
    plt.xlabel('Gameweek')
    plt.ylabel('Player Value')
    plt.show()

# Example 4: Line Plot of Player Points Across Gameweeks (for a specific player)
def plot_player_points_over_time(first_name, second_name):
    player_data = df[(df['first_name'] == first_name) & (df['second_name'] == second_name)]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='event', y='total_points', data=player_data, marker='o', color='green')
    plt.title(f'Total Points Across Gameweeks - {first_name} {second_name}')
    plt.xlabel('Gameweek')
    plt.ylabel('Total Points')
    plt.show()

# Example 5: Line Plot of Player Points Across Gameweeks (for a specific player)
def plot_value_for_money():
    df['value_for_money'] = df['total_points'] / (df['value'] / 10)  # Value is stored as tenths
    top_value_players = df.groupby(['first_name', 'second_name']).mean()['value_for_money'].nlargest(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='value_for_money', y='second_name', data=top_value_players, palette='coolwarm')
    plt.title('Top 10 Players by Value for Money (Points per Million)')
    plt.xlabel('Points per Million')
    plt.ylabel('Player Name')
    plt.show()

# Example 6
def plot_most_selected_players_over_time():
    top_selected_players = df.groupby(['first_name', 'second_name']).mean()['selected'].nlargest(10).reset_index()

    for _, row in top_selected_players.iterrows():
        player_data = df[(df['first_name'] == row['first_name']) & (df['second_name'] == row['second_name'])]

        plt.figure(figsize=(10, 6))
        sns.lineplot(x='event', y='selected', data=player_data, marker='o')
        plt.title(f'Selection Trend - {row["first_name"]} {row["second_name"]}')
        plt.xlabel('Gameweek')
        plt.ylabel('Selected by Managers')
        plt.show()

# Example 7
def plot_cumulative_points(first_name, second_name):
    player_data = df[(df['first_name'] == first_name) & (df['second_name'] == second_name)]
    player_data['cumulative_points'] = player_data['total_points'].cumsum()

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='event', y='cumulative_points', data=player_data, marker='o')
    plt.title(f'Cumulative Points - {first_name} {second_name}')
    plt.xlabel('Gameweek')
    plt.ylabel('Cumulative Points')
    plt.show()

# Example 8
def plot_clean_sheets_by_position():
    gk_and_def = df[df['position'].isin(['Goalkeeper', 'Defender'])]
    top_clean_sheets = gk_and_def.groupby(['first_name', 'second_name', 'position']).sum()['clean_sheets'].nlargest(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='clean_sheets', y='second_name', hue='position', data=top_clean_sheets, palette='Blues')
    plt.title('Top Goalkeepers and Defenders by Clean Sheets')
    plt.xlabel('Clean Sheets')
    plt.ylabel('Player Name')
    plt.show()

# Example 5
def plot_goal_involvement():
    df['goal_involvement'] = df['goals_scored'] + df['assists']
    top_goal_involvers = df.groupby(['first_name', 'second_name']).sum()['goal_involvement'].nlargest(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='goal_involvement', y='second_name', data=top_goal_involvers, palette='Oranges')
    plt.title('Top 10 Players by Goal Involvement (Goals + Assists)')
    plt.xlabel('Goal Involvement')
    plt.ylabel('Player Name')
    plt.show()

# Example 5
def plot_bps_leaderboard():
    top_bps_players = df.groupby(['first_name', 'second_name']).sum()['bps'].nlargest(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='bps', y='second_name', data=top_bps_players, palette='Purples')
    plt.title('Top 10 Players by Bonus Points System (BPS)')
    plt.xlabel('Total BPS')
    plt.ylabel('Player Name')
    plt.show()

# Example 5
def plot_xg_vs_goals():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='expected_goals', y='goals_scored', hue='position', data=df, palette='Set2', s=100)
    plt.title('Expected Goals vs Actual Goals Scored')
    plt.xlabel('Expected Goals (xG)')
    plt.ylabel('Actual Goals Scored')
    plt.show()

# Example 5
def plot_points_heatmap():
    pivot_data = df.pivot_table(index=['first_name', 'second_name'], columns='event', values='total_points', aggfunc='sum')
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_data, cmap='YlGnBu', linewidths=0.5)
    plt.title('Points Scored by Players Across Gameweeks')
    plt.xlabel('Gameweek')
    plt.ylabel('Player')
    plt.show()

# Example 5
def plot_top_players_by_position():
    top_players = df.groupby(['position', 'first_name', 'second_name']).sum()['total_points'].reset_index()
    top_players = top_players.groupby('position').apply(lambda x: x.nlargest(5, 'total_points')).reset_index(drop=True)

    plt.figure(figsize=(12, 8))
    sns.barplot(x='total_points', y='second_name', hue='position', data=top_players, palette='Set3')
    plt.title('Top 5 Players by Total Points in Each Position')
    plt.xlabel('Total Points')
    plt.ylabel('Player Name')
    plt.legend(title='Position')
    plt.show()

# Example 5
def plot_top_players_by_position():
    top_players = df.groupby(['position', 'first_name', 'second_name']).sum()['total_points'].reset_index()
    top_players = top_players.groupby('position').apply(lambda x: x.nlargest(5, 'total_points')).reset_index(drop=True)

    plt.figure(figsize=(12, 8))
    sns.barplot(x='total_points', y='second_name', hue='position', data=top_players, palette='Set3')
    plt.title('Top 5 Players by Total Points in Each Position')
    plt.xlabel('Total Points')
    plt.ylabel('Player Name')
    plt.legend(title='Position')
    plt.show()

# Example 5
def plot_team_performance():
    team_performance = df.groupby('team').sum()['total_points'].reset_index()

    plt.figure(figsize=(12, 8))
    sns.barplot(x='total_points', y='team', data=team_performance, palette='RdYlGn')
    plt.title('Total Points Contribution by Team')
    plt.xlabel('Total Points')
    plt.ylabel('Team')
    plt.show()

def plot_xgi_top_players():
    # Calculate xGI (Expected Goal Involvement)
    df['xGI'] = df['expected_goals'] + df['expected_assists']

    # Group by player and sum their xGI across all gameweeks, then get the top 10
    top_xgi_players = df.groupby(['first_name', 'second_name']).sum()['xGI'].nlargest(10).reset_index()

    # Plot the top 10 players by xGI
    plt.figure(figsize=(10, 6))
    sns.barplot(x='xGI', y='second_name', data=top_xgi_players, palette='magma')
    plt.title('Top 10 Players by Expected Goal Involvement (xGI)')
    plt.xlabel('Expected Goal Involvement (xGI)')
    plt.ylabel('Player Name')
    plt.show()

def plot_xgi_vs_actual_and_over_under():
    # Calculate xGI (Expected Goal Involvement)
    df['xGI'] = df['expected_goals'] + df['expected_assists']

    # Calculate actual goal involvement (Goals + Assists)
    df['actual_GI'] = df['goals_scored'] + df['assists']

    # Calculate over/underperformance (Actual GI - xGI)
    df['over_underperformance'] = df['actual_GI'] - df['xGI']

    # Group by player and sum their stats across all gameweeks
    top_players = df.groupby(['first_name', 'second_name']).sum()[['xGI', 'goals_scored', 'assists', 'actual_GI', 'over_underperformance']].nlargest(10, 'xGI').reset_index()

    # Plot the bars
    fig, ax = plt.subplots(figsize=(14, 8))

    # Set width for the bars
    bar_width = 0.25
    index = range(len(top_players))

    # Bar for xGI
    plt.bar(index, top_players['xGI'], bar_width, label='Expected Goal Involvement (xGI)', color='#6A0DAD', alpha=0.8)

    # Stacked bar for Actual Goals and Assists
    plt.bar([i + bar_width for i in index], top_players['goals_scored'], bar_width, label='Actual Goals', color='#1f77b4', alpha=0.9)
    plt.bar([i + bar_width for i in index], top_players['assists'], bar_width, label='Actual Assists', bottom=top_players['goals_scored'], color='#ff7f0e', alpha=0.9)

    # Bar for Over/Underperformance
    plt.bar([i + 2 * bar_width for i in index], top_players['over_underperformance'], bar_width, label='Over/Underperformance', color='#2ca02c', alpha=0.8)

    # Add labels and title
    plt.xlabel('Player', fontsize=14, labelpad=10)
    plt.ylabel('Goal Involvement', fontsize=14, labelpad=10)
    plt.title('xGI vs Actual Goals + Assists and Over/Underperformance', fontsize=18, fontweight='bold', pad=20)

    # Add player names to x-axis, bolding the last names
    plt.xticks([i + bar_width for i in index], 
               [f"{fn} {ln}" if ln.islower() else f"{fn} {ln.upper()}" for fn, ln in zip(top_players['first_name'], top_players['second_name'])],
               rotation=45, fontsize=12)

    # Add gridlines for readability
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Add legend in the upper right corner
    plt.legend(loc='upper right', fontsize=12)

    # Add numbers on top of the bars for actual goals and assists
    for i, player in enumerate(index):
        # Adjust label positions for goals and assists
        plt.text(i + bar_width, top_players['goals_scored'][i] / 2, f'{top_players["goals_scored"][i]}', ha='center', color='white', fontweight='bold', fontsize=10)
        plt.text(i + bar_width, top_players['goals_scored'][i] + top_players['assists'][i] / 2, f'{top_players["assists"][i]}', ha='center', color='black', fontweight='bold', fontsize=10)

        # Add the xGI values with two decimal places, rotated to fit on the xGI bar
        plt.text(i, top_players['xGI'][i] - 0.1, f'{top_players["xGI"][i]:.2f}', ha='center', va='top', rotation=90, color='white', fontweight='bold', fontsize=10)

        # Add over/underperformance values on the corresponding bar
        plt.text(i + 2 * bar_width, top_players['over_underperformance'][i] - 0.1, f'{top_players["over_underperformance"][i]:.2f}', 
                 ha='center', va='top', rotation=90, color='white', fontweight='bold', fontsize=10)

    plt.tight_layout()
    plt.show()

# Choose the function to execute
if __name__ == "__main__":
    # Uncomment the visualization you want to generate:

    # plot_top_players_by_points()   # Example 1: Top 10 Players by Total Points
    # plot_goals_vs_assists()        # Example 2: Goals Scored vs Assists Scatter Plot
    plot_xgi_vs_actual_and_over_under()
    # plot_top_players_by_position()
    # For specific players like Mohamed Salah:
    # plot_player_value_over_time('Mohamed', 'Salah')  # Example 3: Player Value Over Time
    # plot_player_points_over_time('Mohamed', 'Salah') # Example 4: Player Points Over Time
