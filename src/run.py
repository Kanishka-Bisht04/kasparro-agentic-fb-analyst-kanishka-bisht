import sys
from orchestrator import Orchestrator


def main():
    """
    Entry point of the entire agentic pipeline.
    """
    # Check if user provided a query
    if len(sys.argv) < 2:
        print("❌ Please provide a query. Example:")
        print('   python src/run.py "Analyze ROAS drop"')
        return

    query = sys.argv[1]

    print("\n🚀 Running Agentic FB Analyst Pipeline...")
    print("Your query:", query)

    # Create Orchestrator object
    orchestrator = Orchestrator()

    # Run the orchestrator
    result = orchestrator.run(query)

    print("\n✅ Pipeline completed successfully!")
    print("📁 Check the 'reports/' folder for the output files.")


if __name__ == "__main__":
    main()
