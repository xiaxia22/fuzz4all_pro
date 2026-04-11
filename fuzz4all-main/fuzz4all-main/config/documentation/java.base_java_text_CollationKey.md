# Class CollationKey

**Source:** `java.base\java\text\CollationKey.html`

### Class Description

```java
public abstract class
CollationKey

extends
Object

implements
Comparable
<
CollationKey
>
```

A

CollationKey

represents a

String

under the
rules of a specific

Collator

object. Comparing two

CollationKey

s returns the relative order of the

String

s they represent. Using

CollationKey

s
to compare

String

s is generally faster than using

Collator.compare

. Thus, when the

String

s
must be compared multiple times, for example when sorting a list
of

String

s. It's more efficient to use

CollationKey

s.

You can not create

CollationKey

s directly. Rather,
generate them by calling

Collator.getCollationKey

.
You can only compare

CollationKey

s generated from
the same

Collator

object.

Generating a

CollationKey

for a

String

involves examining the entire

String

and converting it to series of bits that can be compared bitwise. This
allows fast comparisons once the keys are generated. The cost of generating
keys is recouped in faster comparisons when

String

s need
to be compared many times. On the other hand, the result of a comparison
is often determined by the first couple of characters of each

String

.

Collator.compare

examines only as many characters as it needs which
allows it to be faster when doing single comparisons.

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

**All Implemented Interfaces:** Comparable

<

CollationKey

>

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CollationKey​(
String
source)

CollationKey constructor.

**Parameters:**
- source

- the source string

**Throws:**
- NullPointerException

- if

source

is null

**Since:**
- 1.6

---

### Method Details

#### public abstract int compareTo​(
CollationKey
target)

Compare this CollationKey to the target CollationKey. The collation rules of the
Collator object which created these keys are applied.

Note:

CollationKeys created by different Collators can not be compared.

**Specified by:**
- compareTo

in interface

Comparable

<

CollationKey

>

**Parameters:**
- target

- target CollationKey

**Returns:**
- Returns an integer value. Value is less than zero if this is less
than target, value is zero if this and target are equal and value is greater than
zero if this is greater than target.

**See Also:**
- Collator.compare(java.lang.String, java.lang.String)

---

#### public
String
getSourceString()

Returns the String that this CollationKey represents.

**Returns:**
- the source string of this CollationKey

---

#### public abstract byte[] toByteArray()

Converts the CollationKey to a sequence of bits. If two CollationKeys
could be legitimately compared, then one could compare the byte arrays
for each of those keys to obtain the same result. Byte arrays are
organized most significant byte first.

**Returns:**
- a byte array representation of the CollationKey

---

### Additional Sections

#### Class CollationKey

java.lang.Object

- java.text.CollationKey

java.text.CollationKey

**All Implemented Interfaces:** Comparable

<

CollationKey

>

```java
public abstract class
CollationKey

extends
Object

implements
Comparable
<
CollationKey
>
```

A

CollationKey

represents a

String

under the
rules of a specific

Collator

object. Comparing two

CollationKey

s returns the relative order of the

String

s they represent. Using

CollationKey

s
to compare

String

s is generally faster than using

Collator.compare

. Thus, when the

String

s
must be compared multiple times, for example when sorting a list
of

String

s. It's more efficient to use

CollationKey

s.

You can not create

CollationKey

s directly. Rather,
generate them by calling

Collator.getCollationKey

.
You can only compare

CollationKey

s generated from
the same

Collator

object.

Generating a

CollationKey

for a

String

involves examining the entire

String

and converting it to series of bits that can be compared bitwise. This
allows fast comparisons once the keys are generated. The cost of generating
keys is recouped in faster comparisons when

String

s need
to be compared many times. On the other hand, the result of a comparison
is often determined by the first couple of characters of each

String

.

Collator.compare

examines only as many characters as it needs which
allows it to be faster when doing single comparisons.

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

**Since:** 1.1
**See Also:** Collator

,

RuleBasedCollator

public abstract class

CollationKey

extends

Object

implements

Comparable

<

CollationKey

>

A

CollationKey

represents a

String

under the
rules of a specific

Collator

object. Comparing two

CollationKey

s returns the relative order of the

String

s they represent. Using

CollationKey

s
to compare

String

s is generally faster than using

Collator.compare

. Thus, when the

String

s
must be compared multiple times, for example when sorting a list
of

String

s. It's more efficient to use

CollationKey

s.

You can not create

CollationKey

s directly. Rather,
generate them by calling

Collator.getCollationKey

.
You can only compare

CollationKey

s generated from
the same

Collator

object.

Generating a

CollationKey

for a

String

involves examining the entire

String

and converting it to series of bits that can be compared bitwise. This
allows fast comparisons once the keys are generated. The cost of generating
keys is recouped in faster comparisons when

String

s need
to be compared many times. On the other hand, the result of a comparison
is often determined by the first couple of characters of each

String

.

Collator.compare

examines only as many characters as it needs which
allows it to be faster when doing single comparisons.

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

You can not create

CollationKey

s directly. Rather,
generate them by calling

Collator.getCollationKey

.
You can only compare

CollationKey

s generated from
the same

Collator

object.

Generating a

CollationKey

for a

String

involves examining the entire

String

and converting it to series of bits that can be compared bitwise. This
allows fast comparisons once the keys are generated. The cost of generating
keys is recouped in faster comparisons when

String

s need
to be compared many times. On the other hand, the result of a comparison
is often determined by the first couple of characters of each

String

.

Collator.compare

examines only as many characters as it needs which
allows it to be faster when doing single comparisons.

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

Generating a

CollationKey

for a

String

involves examining the entire

String

and converting it to series of bits that can be compared bitwise. This
allows fast comparisons once the keys are generated. The cost of generating
keys is recouped in faster comparisons when

String

s need
to be compared many times. On the other hand, the result of a comparison
is often determined by the first couple of characters of each

String

.

Collator.compare

examines only as many characters as it needs which
allows it to be faster when doing single comparisons.

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

The following example shows how

CollationKey

s might be used
to sort a list of

String

s.

```java
// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());
```

// Create an array of CollationKeys for the Strings to be sorted.
Collator myCollator = Collator.getInstance();
CollationKey[] keys = new CollationKey[3];
keys[0] = myCollator.getCollationKey("Tom");
keys[1] = myCollator.getCollationKey("Dick");
keys[2] = myCollator.getCollationKey("Harry");
sort(keys);

//...

// Inside body of sort routine, compare keys this way
if (keys[i].compareTo(keys[j]) > 0)
// swap keys[i] and keys[j]

//...

// Finally, when we've returned from sort.
System.out.println(keys[0].getSourceString());
System.out.println(keys[1].getSourceString());
System.out.println(keys[2].getSourceString());

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CollationKey

​(

String

source)

CollationKey constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int

compareTo

​(

CollationKey

target)

Compare this CollationKey to the target CollationKey.

String

getSourceString

()

Returns the String that this CollationKey represents.

abstract byte[]

toByteArray

()

Converts the CollationKey to a sequence of bits.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

Modifier

Constructor

Description

protected

CollationKey

​(

String

source)

CollationKey constructor.

---

#### Constructor Summary

CollationKey constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract int

compareTo

​(

CollationKey

target)

Compare this CollationKey to the target CollationKey.

String

getSourceString

()

Returns the String that this CollationKey represents.

abstract byte[]

toByteArray

()

Converts the CollationKey to a sequence of bits.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

Compare this CollationKey to the target CollationKey.

Returns the String that this CollationKey represents.

Converts the CollationKey to a sequence of bits.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

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

- CollationKey

```java
protected CollationKey​(
String
source)
```

CollationKey constructor.

**Parameters:** source

- the source string
**Throws:** NullPointerException

- if

source

is null
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- compareTo

```java
public abstract int compareTo​(
CollationKey
target)
```

Compare this CollationKey to the target CollationKey. The collation rules of the
Collator object which created these keys are applied.

Note:

CollationKeys created by different Collators can not be compared.

**Specified by:** compareTo

in interface

Comparable

<

CollationKey

>
**Parameters:** target

- target CollationKey
**Returns:** Returns an integer value. Value is less than zero if this is less
than target, value is zero if this and target are equal and value is greater than
zero if this is greater than target.
**See Also:** Collator.compare(java.lang.String, java.lang.String)

- getSourceString

```java
public
String
getSourceString()
```

Returns the String that this CollationKey represents.

**Returns:** the source string of this CollationKey

- toByteArray

```java
public abstract byte[] toByteArray()
```

Converts the CollationKey to a sequence of bits. If two CollationKeys
could be legitimately compared, then one could compare the byte arrays
for each of those keys to obtain the same result. Byte arrays are
organized most significant byte first.

**Returns:** a byte array representation of the CollationKey

Constructor Detail

- CollationKey

```java
protected CollationKey​(
String
source)
```

CollationKey constructor.

**Parameters:** source

- the source string
**Throws:** NullPointerException

- if

source

is null
**Since:** 1.6

---

#### Constructor Detail

CollationKey

```java
protected CollationKey​(
String
source)
```

CollationKey constructor.

**Parameters:** source

- the source string
**Throws:** NullPointerException

- if

source

is null
**Since:** 1.6

---

#### CollationKey

protected CollationKey​(

String

source)

CollationKey constructor.

Method Detail

- compareTo

```java
public abstract int compareTo​(
CollationKey
target)
```

Compare this CollationKey to the target CollationKey. The collation rules of the
Collator object which created these keys are applied.

Note:

CollationKeys created by different Collators can not be compared.

**Specified by:** compareTo

in interface

Comparable

<

CollationKey

>
**Parameters:** target

- target CollationKey
**Returns:** Returns an integer value. Value is less than zero if this is less
than target, value is zero if this and target are equal and value is greater than
zero if this is greater than target.
**See Also:** Collator.compare(java.lang.String, java.lang.String)

- getSourceString

```java
public
String
getSourceString()
```

Returns the String that this CollationKey represents.

**Returns:** the source string of this CollationKey

- toByteArray

```java
public abstract byte[] toByteArray()
```

Converts the CollationKey to a sequence of bits. If two CollationKeys
could be legitimately compared, then one could compare the byte arrays
for each of those keys to obtain the same result. Byte arrays are
organized most significant byte first.

**Returns:** a byte array representation of the CollationKey

---

#### Method Detail

compareTo

```java
public abstract int compareTo​(
CollationKey
target)
```

Compare this CollationKey to the target CollationKey. The collation rules of the
Collator object which created these keys are applied.

Note:

CollationKeys created by different Collators can not be compared.

**Specified by:** compareTo

in interface

Comparable

<

CollationKey

>
**Parameters:** target

- target CollationKey
**Returns:** Returns an integer value. Value is less than zero if this is less
than target, value is zero if this and target are equal and value is greater than
zero if this is greater than target.
**See Also:** Collator.compare(java.lang.String, java.lang.String)

---

#### compareTo

public abstract int compareTo​(

CollationKey

target)

Compare this CollationKey to the target CollationKey. The collation rules of the
Collator object which created these keys are applied.

Note:

CollationKeys created by different Collators can not be compared.

getSourceString

```java
public
String
getSourceString()
```

Returns the String that this CollationKey represents.

**Returns:** the source string of this CollationKey

---

#### getSourceString

public

String

getSourceString()

Returns the String that this CollationKey represents.

toByteArray

```java
public abstract byte[] toByteArray()
```

Converts the CollationKey to a sequence of bits. If two CollationKeys
could be legitimately compared, then one could compare the byte arrays
for each of those keys to obtain the same result. Byte arrays are
organized most significant byte first.

**Returns:** a byte array representation of the CollationKey

---

#### toByteArray

public abstract byte[] toByteArray()

Converts the CollationKey to a sequence of bits. If two CollationKeys
could be legitimately compared, then one could compare the byte arrays
for each of those keys to obtain the same result. Byte arrays are
organized most significant byte first.

---

