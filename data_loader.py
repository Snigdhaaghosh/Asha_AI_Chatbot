import json
import pandas as pd
import os

class DataLoader:
    def __init__(self):
        self.job_listings = None
        self.session_details = None
        self.mentorship_programs = None
        self.load_data()

    def load_data(self):
        try:
            # Load job listings
            if os.path.exists('job_listing_data.csv'):
                self.job_listings = pd.read_csv('job_listing_data.csv')
            
            # Load session details
            if os.path.exists('session_details.json'):
                with open('session_details.json', 'r') as f:
                    self.session_details = json.load(f)
            
            # Load mentorship programs
            if os.path.exists('mentorship_programs.json'):
                with open('mentorship_programs.json', 'r') as f:
                    self.mentorship_programs = json.load(f)
        except Exception as e:
            print(f"Error loading data: {str(e)}")

    def get_job_listings(self, filters=None):
        if self.job_listings is None:
            return []
        
        if filters:
            filtered_data = self.job_listings
            for key, value in filters.items():
                if key in self.job_listings.columns:
                    filtered_data = filtered_data[filtered_data[key] == value]
            return filtered_data.to_dict('records')
        return self.job_listings.to_dict('records')

    def get_session_details(self, session_id=None):
        if self.session_details is None:
            return []
        
        if session_id:
            return [session for session in self.session_details if session['id'] == session_id]
        return self.session_details

    def get_mentorship_programs(self, filters=None):
        if self.mentorship_programs is None:
            return []
        
        if filters:
            filtered_data = self.mentorship_programs
            for key, value in filters.items():
                filtered_data = [program for program in filtered_data if program.get(key) == value]
            return filtered_data
        return self.mentorship_programs 