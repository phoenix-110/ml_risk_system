import torch 
import torch.nn as nn
import numpy as np
from torch.utils.data import Dataset

class LSTMRiskModel(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int = 32):
        super().__init__()
        self.lstm=nn.LSTM(input_size=input_dim,hidden_size=hidden_dim,batch_first=True)
        self.fc=nn.Linear(hidden_dim,1)
        self.sigmoid=nn.Sigmoid()
    def forward(self,x):
        # x shape: (batch, sequence_length, features)
        out,_=self.lstm(x)
        out=out[:,-1,:]
        out=self.fc(out)
        return self.sigmoid(out)





class SequenceDataset(Dataset):
    def __init__(self, X, y, seq_len: int = 30):
        self.X = X.values.astype("float32")
        self.y = y.values.astype("float32")
        self.seq_len = seq_len

    def __len__(self):
        return len(self.X) - self.seq_len

    def __getitem__(self, idx):
        x_seq = self.X[idx : idx + self.seq_len]
        y_label = self.y[idx + self.seq_len]
        return torch.tensor(x_seq), torch.tensor(y_label)
