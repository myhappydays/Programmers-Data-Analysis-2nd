import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(file_path):
    """Read a CSV file and return the dataframe."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

def get_user_input():
    """Get user input for the type of visualization and column names."""
    try:
        print("Enter the type of visualization (1: histogram, 2: bar, 3: pie chart, 4: boxplot, 5: line, 6: scatter, 7: time series, 8: heatmap, 9: scatterplot matrix, 10: table info, 0: exit):")
        plot_type = input().strip()

        if plot_type not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
            print("Invalid visualization type. Please try again.")
            return get_user_input()

        if plot_type in ['0', '10']:  # Exit or Table info do not require columns
            return plot_type, None, None

        print("Enter the column name:")
        column1 = input().strip()

        column2 = None
        print("Enter the second column name (optional, press Enter to skip):")
        column2 = input().strip()
        if column2 == '':
            column2 = None

        return plot_type, column1, column2
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None

def validate_columns(df, columns):
    """Validate if columns exist in the dataframe."""
    for col in columns:
        if col is not None and col not in df.columns:
            print(f"Error: Column '{col}' not found in the dataframe.")
            return False
    return True

def visualize_data(df, plot_type, column1, column2=None):
    """Generate and display the requested visualization."""
    if not validate_columns(df, [column1, column2]):
        return

    try:
        plt.figure(figsize=(10, 6))

        if plot_type == '1':  # Histogram
            if column2 is None:
                df[column1].hist(bins=30, edgecolor='black')
                plt.title(f'Histogram of {column1}')
                plt.xlabel(column1)
                plt.ylabel('Frequency')
            else:
                label=[column1, column2]
                plt.hist([df[column1], df[column2]], bins=30, edgecolor='black', label=label)
                plt.xlabel(column1)
                plt.ylabel(column2)
                # plt.legend()
                plt.title(f'Histogram of {column1}, {column2}')

        elif plot_type == '2':  # Bar plot
            df[column1].value_counts().plot(kind='bar', edgecolor='black')
            plt.title(f'Bar plot of {column1}')
            plt.xlabel(column1)
            plt.ylabel('Count')

        elif plot_type == '3':  # Pie chart
            df[column1].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title(f'Pie chart of {column1}')
            plt.ylabel('')

        elif plot_type == '4':  # Boxplot
            df.boxplot(column=[column1])
            plt.title(f'Boxplot of {column1}')
            plt.ylabel(column1)

        elif plot_type == '5':  # Line plot
            df[column1].plot(kind='line')
            plt.title(f'Line plot of {column1}')
            plt.xlabel('Index')
            plt.ylabel(column1)

        elif plot_type == '6':  # Scatter plot
            if column2:
                plt.scatter(df[column1], df[column2], alpha=0.5)
                plt.title(f'Scatter plot between {column1} and {column2}')
                plt.xlabel(column1)
                plt.ylabel(column2)
            else:
                print("Scatter plot requires two columns. Please provide a second column name.")

        elif plot_type == '7':  # Time series
            df[column1] = pd.to_datetime(df[column1])
            df.set_index(column1).plot()
            plt.title(f'Time series of {column1}')
            plt.xlabel('Time')
            plt.ylabel('Value')

        elif plot_type == '8':  # Heatmap
            correlation_matrix = df.corr()
            sns.heatmap(correlation_matrix, annot=True, linewidths=.5, cmap='coolwarm')
            plt.title('Heatmap of Correlation Matrix')
            plt.show()

        elif plot_type == '9':  # Scatterplot Matrix
            if column2:
                sns.pairplot(df[[column1, column2]])
                plt.suptitle(f'Scatterplot Matrix of {column1} and {column2}')
            else:
                sns.pairplot(df)
                plt.suptitle('Scatterplot Matrix')
            plt.show()

        elif plot_type == '10':  # Table info
            print(df.info())
            print(df.describe())
            return

        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred while generating the plot: {e}")

def main():
    """Main function to execute the data visualization tool."""
    file_path = 'E:\\2024 프로그래머스 데이터 분석 데브코스\\데이터 분석\\9주차\\2차프로젝트\\Programmer-Data-Analysis-2nd\\data\\BankChurners.csv'

    df = read_csv(file_path)

    if df is None:
        return

    while True:
        plot_type, column1, column2 = get_user_input()

        if plot_type == '0':  # Exit
            print("Exiting visualization tool.")
            break

        visualize_data(df, plot_type, column1, column2)

if __name__ == "__main__":
    main()
