import yahooquery as yq
import pandas as pd

# Load S&P 500 and S&P 400 symbols from a file or manually define them
sp500_symbols = [
'MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 
'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AEP', 'AXP', 'AIG', 
'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'APO', 'AAPL', 'AMAT', 'APTV', 
'ACGL', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 
'BAC', 'BAX', 'BDX', 'BRK.B', 'BBY', 'TECH', 'BIIB', 'BLK', 'BX', 'BK', 'BA', 'BKNG', 'BWA', 'BSX', 'BMY', 
'AVGO', 'BR', 'BRO', 'BF.B', 'BLDR', 'BG', 'BXP', 'CHRW', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 
'CCL', 'CARR', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CRL', 'SCHW', 'CHTR', 
'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 
'CMCSA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CPAY', 'CTVA', 'CSGP', 'COST', 'CTRA', 'CRWD', 
'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DECK', 'DE', 'DELL', 'DAL', 'DVN', 'DXCM', 'FANG', 'DLR', 
'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 
'EA', 'ELV', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ERIE', 'ESS', 'EL', 'EG', 'EVRG', 
'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 
'FI', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 'GRMN', 'IT', 'GE', 'GEHC', 'GEV', 'GEN', 'GNRC', 'GD', 
'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GDDY', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 
'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 
'ITW', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV', 'IRM', 
'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB', 'KIM', 
'KMI', 'KKR', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LII', 'LLY', 'LIN', 'LYV', 
'LKQ', 'LMT', 'L', 'LOW', 'LULU', 'LYB', 'MTB', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 
'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 
'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 
'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 
'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PLTR', 'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 
'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 
'PTC', 'PSA', 'PHM', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 
'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SJM', 
'SW', 'SNA', 'SOLV', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SMCI', 'SYF', 'SNPS', 'SYY', 'TMUS', 
'TROW', 'TTWO', 'TPR', 'TRGP', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TPL', 'TXT', 'TMO', 'TJX', 'TSCO', 
'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 
'UHS', 'VLO', 'VTR', 'VLTO', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VTRS', 'VICI', 'V', 'VST', 'VMC', 'WRB', 'GWW', 'WAB', 
'WBA', 'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WY', 'WMB', 'WTW', 'WDAY', 'WYNN', 
'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZTS'
]

sp400_symbols = [
'AA', 'AAL', 'AAON', 'ACHC', 'ACM', 'ADC', 'AFG', 'AGCO', 'AIT', 'ALE', 'ALGM', 'ALLY', 'ALTR', 'ALV', 'AM', 'AMED', 
'AMG', 'AMH', 'AMKR', 'AN', 'ANF', 'APPF', 'AR', 'ARMK', 'ARW', 'ASB', 'ASGN', 'ASH', 'ATR', 'AVNT', 'AVT', 'AVTR', 
'AXTA', 'AYI', 'AZPN', 'BC', 'BCO', 'BDC', 'BERY', 'BHF', 'BILL', 'BIO', 'BJ', 'BKH', 'BLD', 'BLKB', 'BMRN', 'BRBR', 
'BRKR', 'BRX', 'BURL', 'BWXT', 'BYD', 'CACI', 'CADE', 'CAR', 'CART', 'CASY', 'CBSH', 'CBT', 'CC', 'CCK', 'CDP', 'CELH', 
'CFR', 'CG', 'CGNX', 'CHDN', 'CHE', 'CHH', 'CHRD', 'CHWY', 'CHX', 'CIEN', 'CIVI', 'CLF', 'CLH', 'CMA', 'CMC', 'CNH', 
'CNM', 'CNO', 'CNX', 'CNXC', 'COHR', 'COKE', 'COLB', 'COLM', 'COTY', 'CPRI', 'CR', 'CROX', 'CRS', 'CRUS', 'CSL', 'CUBE', 
'CUZ', 'CVLT', 'CW', 'CXT', 'CYTK', 'DAR', 'DBX', 'DCI', 'DINO', 'DKS', 'DLB', 'DOCS', 'DOCU', 'DT', 'DTM', 'DUOL', 
'EEFT', 'EGP', 'EHC', 'ELF', 'ELS', 'EME', 'ENS', 'ENSG', 'ENTG', 'EPR', 'EQH', 'ESAB', 'ESNT', 'EVR', 'EWBC', 'EXE', 
'EXEL', 'EXLS', 'EXP', 'EXPO', 'FAF', 'FBIN', 'FCFS', 'FCN', 'FFIN', 'FHI', 'FHN', 'FIVE', 'FIX', 'FLEX', 'FLG', 'FLO', 
'FLR', 'FLS', 'FN', 'FNB', 'FND', 'FNF', 'FOUR', 'FR', 'FYBR', 'G', 'GAP', 'GATX', 'GBCI', 'GEF', 'GGG', 'GHC', 'GLPI', 
'GME', 'GMED', 'GNTX', 'GPK', 'GT', 'GTLS', 'GWRE', 'GXO', 'H', 'HAE', 'HALO', 'HGV', 'HLI', 'HLNE', 'HOG', 'HOMB', 
'HQY', 'HR', 'HRB', 'HWC', 'HXL', 'IBKR', 'IBOC', 'IDA', 'ILMN', 'INGR', 'IPGP', 'IRDM', 'IRT', 'ITT', 'JAZZ', 'JEF', 
'JHG', 'JLL', 'JWN', 'KBH', 'KBR', 'KD', 'KEX', 'KMPR', 'KNF', 'KNSL', 'KNX', 'KRC', 'KRG', 'LAD', 'LAMR', 'LANC', 
'LEA', 'LECO', 'LFUS', 'LITE', 'LIVN', 'LNTH', 'LNW', 'LOPE', 'LPX', 'LSCC', 'LSTR', 'M', 'MAN', 'MANH', 'MASI', 'MAT', 
'MEDP', 'MIDD', 'MKSI', 'MLI', 'MMS', 'MORN', 'MSA', 'MSM', 'MTDR', 'MTG', 'MTN', 'MTSI', 'MTZ', 'MUR', 'MUSA', 'NBIX', 
'NEOG', 'NEU', 'NFG', 'NJR', 'NLY', 'NNN', 'NOV', 'NOVT', 'NSA', 'NSP', 'NVST', 'NVT', 'NWE', 'NXST', 'NXT', 'NYT', 
'OC', 'OGE', 'OGS', 'OHI', 'OLED', 'OLLI', 'OLN', 'ONB', 'ONTO', 'OPCH', 'ORA', 'ORI', 'OSK', 'OVV', 'OZK', 'PAG', 
'PB', 'PBF', 'PCH', 'PCTY', 'PEN', 'PFGC', 'PII', 'PK', 'PLNT', 'PNFP', 'POR', 'POST', 'POWI', 'PPC', 'PR', 'PRGO', 
'PRI', 'PSN', 'PSTG', 'PVH', 'QLYS', 'R', 'RBA', 'RBC', 'REXR', 'RGA', 'RGEN', 'RGLD', 'RH', 'RLI', 'RMBS', 'RNR', 
'ROIV', 'RPM', 'RRC', 'RRX', 'RS', 'RYAN', 'RYN', 'SAIA', 'SAIC', 'SAM', 'SBRA', 'SCI', 'SEIC', 'SF', 'SFM', 'SGI', 
'SHC', 'SIGI', 'SKX', 'SLAB', 'SLGN', 'SLM', 'SMG', 'SNV', 'SNX', 'SON', 'SR', 'SRPT', 'SSB', 'SSD', 'ST', 'STAG', 
'STWD', 'SWX', 'SYNA', 'TCBI', 'TDC', 'TEX', 'THC', 'THG', 'THO', 'TKO', 'TKR', 'TMHC', 'TNL', 'TOL', 'TREX', 'TTC', 
'TTEK', 'TXNM', 'TXRH', 'UA', 'UAA', 'UBSI', 'UFPI', 'UGI', 'UMBF', 'UNM', 'USFD', 'UTHR', 'VAC', 'VAL', 'VC', 'VLY', 
'VMI', 'VNO', 'VNOM', 'VNT', 'VOYA', 'VVV', 'WAL', 'WBS', 'WCC', 'WEN', 'WEX', 'WFRD', 'WH', 'WHR', 'WING', 'WLK', 
'WMG', 'WMS', 'WPC', 'WSM', 'WSO', 'WTFC', 'WTRG', 'WTS', 'WU', 'WWD', 'X', 'XPO', 'XRAY', 'YETI', 'ZI', 'ZION'
]  

all_symbols = sp500_symbols + sp400_symbols

# Fetch data
fields = ["symbol", "longName", "marketCap", "sharesOutstanding", "trailingEps", "trailingPE"]
data = yq.Ticker(all_symbols).quote_summary(["summaryDetail", "defaultKeyStatistics"])

# Extract relevant data
records = []
for symbol in all_symbols:
    info = data.get(symbol, {})
    details = info.get("summaryDetail", {})
    stats = info.get("defaultKeyStatistics", {})

    record = {
        "symbol": symbol,
        "name": info.get("quoteType", {}).get("longName", ""),
        "market_cap": details.get("marketCap", {}).get("raw", ""),
        "shares_outstanding": stats.get("sharesOutstanding", {}).get("raw", ""),
        "eps": stats.get("trailingEps", {}).get("raw", ""),
        "pe_ratio": stats.get("trailingPE", {}).get("raw", ""),
    }
    records.append(record)

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("sp_securities.csv", index=False)

print("CSV file saved: sp_securities.csv")
"""


"""