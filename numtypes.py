#!/usr/bin/env python
# -*- coding: utf-8 -*-

FLOATVAR = 0.1

from decimal import Decimal
DECIMALVAR = Decimal('0.1')
print(DECIMALVAR)

from fractions import Fraction
FRACTIONVAR = Fraction(1, 10)
print(FRACTIONVAR)

DF_EQUALITY = DECIMALVAR == FRACTIONVAR

ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
