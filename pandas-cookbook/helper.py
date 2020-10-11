# -*- coding: utf-8 -*-


# https://stackoverflow.com/questions/41680533/is-coding-utf-8-also-a-comment-in-python

# TODO: Writing a doctring for a class
class ColumnNameCleaner:
    ''' Helper class for cleaning the column names'''
    
    def __init__(self, trim_wspace=True, wspace_replacer='_', lower=False):
        self.trim_wspace = trim_wspace
        self.lower = lower
        self.wspace_replacer = wspace_replacer
        
    def clean(self, cols):
        clean_cols = []
        for col in cols:
            if self.trim_wspace:
                col = self._trim_wspace(col)
                
            if self.wspace_replacer is not None:
                col = self._wspace_replacer(col, self.wspace_replacer)
            
            if self.lower:
                col = self._lower(col)
                
        
            clean_cols.append(col)
            
        return clean_cols
            
    @staticmethod    
    def _trim_wspace(s):
        return s.strip()
    
    @staticmethod
    def _wspace_replacer(s, repl):
        return s.replace(' ', repl)
    
    
    @staticmethod 
    def _lower(s):
        return s.lower()
    
