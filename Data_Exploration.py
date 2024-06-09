import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read the CSV file
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

# Function to get user input
def get_user_input():
    try:
        print("Enter the type of visualization (1: histogram, 2: scatter, 3: time series, 4: bar, 5: boxplot, 6: line, 7: scatterplot matrix, 8: heatmap, 9: table info, 0: exit):")
        plot_type = input().strip()

        if plot_type not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid visualization type. Please try again.")
            return get_user_input()

        if plot_type == '0':  # Exit condition
            return plot_type, None, None

        if plot_type == '9':  # Table info does not require specific columns
            return plot_type, None, None

        if plot_type in ['2', '7']:  # Scatter plot and scatterplot matrix require another column
            print("Enter the second column name:")
            column_name_2 = input().strip()
            return plot_type, column_name_2, None

        print("Enter the column name:")
        column_name = input().strip()

        return plot_type, column_name, None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None

# Function to visualize data
def visualize_data(df, plot_type, column1, column2=None):
    try:
        plt.figure(figsize=(10, 6))

        if plot_type == '1':  # Histogram
            df[column1].hist(bins=30, edgecolor='black')
            plt.title(f'Histogram of {column1}')
            plt.xlabel(column1)
            plt.ylabel('Frequency')

        elif plot_type == '2':  # Scatter plot
            plt.scatter(df[column1], df[column2], alpha=0.5)
            plt.title(f'Scatter plot between {column1} and {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)

        elif plot_type == '3':  # Time series
            df[column1] = pd.to_datetime(df[column1])
            df.set_index(column1).plot()
            plt.title(f'Time series of {column1}')
            plt.xlabel('Time')
            plt.ylabel('Value')

        elif plot_type == '4':  # Bar plot
            df[column1].value_counts().plot(kind='bar', edgecolor='black')
            plt.title(f'Bar plot of {column1}')
            plt.xlabel(column1)
            plt.ylabel('Count')

        elif plot_type == '5':  # Boxplot
            df.boxplot(column=[column1])
            plt.title(f'Boxplot of {column1}')
            plt.ylabel(column1)

        elif plot_type == '6':  # Line plot
            df[column1].plot(kind='line')
            plt.title(f'Line plot of {column1}')
            plt.xlabel('Index')
            plt.ylabel(column1)

        elif plot_type == '7':  # Scatterplot Matrix
            sns.pairplot(df)
            plt.suptitle(f'Scatterplot Matrix')
            plt.show()

        elif plot_type == '8':  # Heatmap
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            plt.title(f'Heatmap of Correlation Matrix')
            plt.show()

        elif plot_type == '9':  # Table info
            print(df.info())
            return

        plt.show()
    except KeyError as e:
        print(f"Error: Column '{e.args[0]}' not found in the dataframe.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function
def main():
    # File path
    file_path = 'E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\waze_app_dataset.csv'

    # Read the CSV file
    df = read_csv(file_path)

    if df is None:
        return

    # Main loop to get user input and visualize data
    while True:
        plot_type, column1, column2 = get_user_input()

        if plot_type == '0':  # Exit
            print("Exiting visualization tool.")
            break

        visualize_data(df, plot_type, column1, column2)

if __name__ == "__main__":
    main()
