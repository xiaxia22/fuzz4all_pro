# Class ECFieldF2m

**Source:** `java.base\java\security\spec\ECFieldF2m.html`

### Class Description

```java
public class
ECFieldF2m

extends
Object

implements
ECField
```

This immutable class defines an elliptic curve (EC)
characteristic 2 finite field.

**All Implemented Interfaces:** ECField

---

### Field Details

*No entries found.*

### Constructor Details

#### public ECFieldF2m​(int m)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

**Parameters:**
- m

- with 2^

m

being the number of elements.

**Throws:**
- IllegalArgumentException

- if

m

is not positive.

---

#### public ECFieldF2m​(int m,

BigInteger
rp)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.
The reduction polynomial for this field is based
on

rp

whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

**Parameters:**
- m

- with 2^

m

being the number of elements.
- rp

- the BigInteger whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

**Throws:**
- NullPointerException

- if

rp

is null.
- IllegalArgumentException

- if

m

is not positive, or

rp

does not represent
a valid reduction polynomial.

---

#### public ECFieldF2m​(int m,
int[] ks)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis. The reduction polynomial for this
field is based on

ks

whose content
contains the order of the middle term(s) of the
reduction polynomial.
Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1), so

ks

should
have length 1 or 3.

**Parameters:**
- m

- with 2^

m

being the number of elements.
- ks

- the order of the middle term(s) of the
reduction polynomial. Contents of this array are copied
to protect against subsequent modification.

**Throws:**
- NullPointerException

- if

ks

is null.
- IllegalArgumentException

- if

m

is not positive, or the length of

ks

is neither 1 nor 3, or values in

ks

are not between

m

-1 and 1 (inclusive)
and in descending order.

---

### Method Details

#### public int getFieldSize()

Returns the field size in bits which is

m

for this characteristic 2 finite field.

**Specified by:**
- getFieldSize

in interface

ECField

**Returns:**
- the field size in bits.

---

#### public int getM()

Returns the value

m

of this characteristic
2 finite field.

**Returns:**
- m

with 2^

m

being the
number of elements.

---

#### public
BigInteger
getReductionPolynomial()

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:**
- a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

---

#### public int[] getMidTermsOfReductionPolynomial()

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:**
- an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis. A new array is returned
each time this method is called.

---

#### public boolean equals​(
Object
obj)

Compares this finite field for equality with the
specified object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared.

**Returns:**
- true if

obj

is an instance
of ECFieldF2m and both

m

and the reduction
polynomial match, false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this characteristic 2
finite field.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class ECFieldF2m

java.lang.Object

- java.security.spec.ECFieldF2m

java.security.spec.ECFieldF2m

**All Implemented Interfaces:** ECField

```java
public class
ECFieldF2m

extends
Object

implements
ECField
```

This immutable class defines an elliptic curve (EC)
characteristic 2 finite field.

**Since:** 1.5
**See Also:** ECField

public class

ECFieldF2m

extends

Object

implements

ECField

This immutable class defines an elliptic curve (EC)
characteristic 2 finite field.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ECFieldF2m

​(int m)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

ECFieldF2m

​(int m,
int[] ks)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.

ECFieldF2m

​(int m,

BigInteger

rp)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this finite field for equality with the
specified object.

int

getFieldSize

()

Returns the field size in bits which is

m

for this characteristic 2 finite field.

int

getM

()

Returns the value

m

of this characteristic
2 finite field.

int[]

getMidTermsOfReductionPolynomial

()

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

BigInteger

getReductionPolynomial

()

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

int

hashCode

()

Returns a hash code value for this characteristic 2
finite field.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

ECFieldF2m

​(int m)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

ECFieldF2m

​(int m,
int[] ks)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.

ECFieldF2m

​(int m,

BigInteger

rp)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.

---

#### Constructor Summary

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this finite field for equality with the
specified object.

int

getFieldSize

()

Returns the field size in bits which is

m

for this characteristic 2 finite field.

int

getM

()

Returns the value

m

of this characteristic
2 finite field.

int[]

getMidTermsOfReductionPolynomial

()

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

BigInteger

getReductionPolynomial

()

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

int

hashCode

()

Returns a hash code value for this characteristic 2
finite field.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Compares this finite field for equality with the
specified object.

Returns the field size in bits which is

m

for this characteristic 2 finite field.

Returns the value

m

of this characteristic
2 finite field.

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

Returns a hash code value for this characteristic 2
finite field.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ECFieldF2m

```java
public ECFieldF2m​(int m)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

**Parameters:** m

- with 2^

m

being the number of elements.
**Throws:** IllegalArgumentException

- if

m

is not positive.

- ECFieldF2m

```java
public ECFieldF2m​(int m,

BigInteger
rp)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.
The reduction polynomial for this field is based
on

rp

whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** rp

- the BigInteger whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.
**Throws:** NullPointerException

- if

rp

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or

rp

does not represent
a valid reduction polynomial.

- ECFieldF2m

```java
public ECFieldF2m​(int m,
int[] ks)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis. The reduction polynomial for this
field is based on

ks

whose content
contains the order of the middle term(s) of the
reduction polynomial.
Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1), so

ks

should
have length 1 or 3.

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** ks

- the order of the middle term(s) of the
reduction polynomial. Contents of this array are copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

ks

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or the length of

ks

is neither 1 nor 3, or values in

ks

are not between

m

-1 and 1 (inclusive)
and in descending order.

============ METHOD DETAIL ==========

- Method Detail

- getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is

m

for this characteristic 2 finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

- getM

```java
public int getM()
```

Returns the value

m

of this characteristic
2 finite field.

**Returns:** m

with 2^

m

being the
number of elements.

- getReductionPolynomial

```java
public
BigInteger
getReductionPolynomial()
```

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

- getMidTermsOfReductionPolynomial

```java
public int[] getMidTermsOfReductionPolynomial()
```

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis. A new array is returned
each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldF2m and both

m

and the reduction
polynomial match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this characteristic 2
finite field.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- ECFieldF2m

```java
public ECFieldF2m​(int m)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

**Parameters:** m

- with 2^

m

being the number of elements.
**Throws:** IllegalArgumentException

- if

m

is not positive.

- ECFieldF2m

```java
public ECFieldF2m​(int m,

BigInteger
rp)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.
The reduction polynomial for this field is based
on

rp

whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** rp

- the BigInteger whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.
**Throws:** NullPointerException

- if

rp

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or

rp

does not represent
a valid reduction polynomial.

- ECFieldF2m

```java
public ECFieldF2m​(int m,
int[] ks)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis. The reduction polynomial for this
field is based on

ks

whose content
contains the order of the middle term(s) of the
reduction polynomial.
Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1), so

ks

should
have length 1 or 3.

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** ks

- the order of the middle term(s) of the
reduction polynomial. Contents of this array are copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

ks

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or the length of

ks

is neither 1 nor 3, or values in

ks

are not between

m

-1 and 1 (inclusive)
and in descending order.

---

#### Constructor Detail

ECFieldF2m

```java
public ECFieldF2m​(int m)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

**Parameters:** m

- with 2^

m

being the number of elements.
**Throws:** IllegalArgumentException

- if

m

is not positive.

---

#### ECFieldF2m

public ECFieldF2m​(int m)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with normal basis.

ECFieldF2m

```java
public ECFieldF2m​(int m,

BigInteger
rp)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.
The reduction polynomial for this field is based
on

rp

whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** rp

- the BigInteger whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.
**Throws:** NullPointerException

- if

rp

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or

rp

does not represent
a valid reduction polynomial.

---

#### ECFieldF2m

public ECFieldF2m​(int m,

BigInteger

rp)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis.
The reduction polynomial for this field is based
on

rp

whose i-th bit corresponds to
the i-th coefficient of the reduction polynomial.

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1).

ECFieldF2m

```java
public ECFieldF2m​(int m,
int[] ks)
```

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis. The reduction polynomial for this
field is based on

ks

whose content
contains the order of the middle term(s) of the
reduction polynomial.
Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1), so

ks

should
have length 1 or 3.

**Parameters:** m

- with 2^

m

being the number of elements.
**Parameters:** ks

- the order of the middle term(s) of the
reduction polynomial. Contents of this array are copied
to protect against subsequent modification.
**Throws:** NullPointerException

- if

ks

is null.
**Throws:** IllegalArgumentException

- if

m

is not positive, or the length of

ks

is neither 1 nor 3, or values in

ks

are not between

m

-1 and 1 (inclusive)
and in descending order.

---

#### ECFieldF2m

public ECFieldF2m​(int m,
int[] ks)

Creates an elliptic curve characteristic 2 finite
field which has 2^

m

elements with
polynomial basis. The reduction polynomial for this
field is based on

ks

whose content
contains the order of the middle term(s) of the
reduction polynomial.
Note: A valid reduction polynomial is either a
trinomial (X^

m

+ X^

k

+ 1
with

m

>

k

>= 1) or a
pentanomial (X^

m

+ X^

k3

+ X^

k2

+ X^

k1

+ 1 with

m

>

k3

>

k2

>

k1

>= 1), so

ks

should
have length 1 or 3.

Method Detail

- getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is

m

for this characteristic 2 finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

- getM

```java
public int getM()
```

Returns the value

m

of this characteristic
2 finite field.

**Returns:** m

with 2^

m

being the
number of elements.

- getReductionPolynomial

```java
public
BigInteger
getReductionPolynomial()
```

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

- getMidTermsOfReductionPolynomial

```java
public int[] getMidTermsOfReductionPolynomial()
```

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis. A new array is returned
each time this method is called.

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldF2m and both

m

and the reduction
polynomial match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this characteristic 2
finite field.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getFieldSize

```java
public int getFieldSize()
```

Returns the field size in bits which is

m

for this characteristic 2 finite field.

**Specified by:** getFieldSize

in interface

ECField
**Returns:** the field size in bits.

---

#### getFieldSize

public int getFieldSize()

Returns the field size in bits which is

m

for this characteristic 2 finite field.

getM

```java
public int getM()
```

Returns the value

m

of this characteristic
2 finite field.

**Returns:** m

with 2^

m

being the
number of elements.

---

#### getM

public int getM()

Returns the value

m

of this characteristic
2 finite field.

getReductionPolynomial

```java
public
BigInteger
getReductionPolynomial()
```

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

---

#### getReductionPolynomial

public

BigInteger

getReductionPolynomial()

Returns a BigInteger whose i-th bit corresponds to the
i-th coefficient of the reduction polynomial for polynomial
basis or null for normal basis.

getMidTermsOfReductionPolynomial

```java
public int[] getMidTermsOfReductionPolynomial()
```

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

**Returns:** an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis. A new array is returned
each time this method is called.

---

#### getMidTermsOfReductionPolynomial

public int[] getMidTermsOfReductionPolynomial()

Returns an integer array which contains the order of the
middle term(s) of the reduction polynomial for polynomial
basis or null for normal basis.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this finite field for equality with the
specified object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared.
**Returns:** true if

obj

is an instance
of ECFieldF2m and both

m

and the reduction
polynomial match, false otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this finite field for equality with the
specified object.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this characteristic 2
finite field.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this characteristic 2
finite field.

---

