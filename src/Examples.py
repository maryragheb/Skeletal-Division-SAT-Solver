import SkeletalDivision

# Examples
SkeletalDivision.skeletalDivision('5 / 1 = 5',
                 ['5', 
                  '0'])

SkeletalDivision.skeletalDivision('101 / 8 = AB.CDE', 
                 ['F',
                  'GH',
                  'IJ',
                  'KL',
                  'MN',
                  'OP',
                  'QR',
                  'ST',
                  'UV',
                  '0'],
                  limit=3)

SkeletalDivision.skeletalDivision('1365 / 14 == 97.5',
                         ['126', 
                          '105',
                          '98',    
                          '70',
                          '70',
                          '0'],
                         limit = 10)
SkeletalDivision.skeletalDivision('FGHJ / AB == CD.E',
                         ['KL6', 
                          'MNP',
                          'QR',
                          'ST',
                          'UV',
                          '0'],
                         limit = 3)

SkeletalDivision.skeletalDivision('638897 / 749 == 853',
                         ['5992',
                          '3969',
                          '3745',
                          '2247',
                          '2247',
                          '0'],
                         limit = 5)             
SkeletalDivision.skeletalDivision('ZA8BCD / EF9 == G53',
                         ['HIJ2',
                          'K9LM',
                          'NO4P',
                          'QR4S',
                          'TUVW',
                          '0'],
                         limit = 10)

SkeletalDivision.skeletalDivision('101 / 4 = 25.25', 
                 ['8',
                  '21',
                  '20',
                  '10',
                  '8',
                  '20',
                  '20',
                  '0'], limit = 3)
SkeletalDivision.skeletalDivision('BCD / E = FG.HI', 
                 ['J',
                  'KL',
                  'MN',
                  'OP',
                  'Q',
                  'RS',
                  'TU',
                  '0'], limit = 3)

# Feynman's Problem
SkeletalDivision.skeletalDivision('3527876 / 484 == 7289',
                         ['3388', 
                          '1398',
                          '968',    
                          '4307',
                          '3872',
                          '4356',
                          '4356',
                          '0'],
                         limit = 10)
SkeletalDivision.skeletalDivision('BCDEAFG / HAI == JKAL',
                                  ['MNAA', 
                                   'OPQA',
                                   'RSA',    
                                   'TUVW',
                                   'XAYZ',
                                   'abcd',
                                   'efgh',
                                   '0'],
                                  limit = 1)

pass