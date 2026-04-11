# Class AccessibleRelationSet

**Source:** `java.desktop\javax\accessibility\AccessibleRelationSet.html`

### Class Description

```java
public class
AccessibleRelationSet

extends
Object
```

Class

AccessibleRelationSet

determines a component's relation set.
The relation set of a component is a set of

AccessibleRelation

objects that describe the component's relationships with other components.

**Since:** 1.3
**See Also:** AccessibleRelation

---

### Field Details

#### protected
Vector
<
AccessibleRelation
> relations

Each entry in the

Vector

represents an

AccessibleRelation

.

**See Also:**
- add(javax.accessibility.AccessibleRelation)

,

addAll(javax.accessibility.AccessibleRelation[])

,

remove(javax.accessibility.AccessibleRelation)

,

contains(java.lang.String)

,

get(java.lang.String)

,

size()

,

toArray()

,

clear()

---

### Constructor Details

#### public AccessibleRelationSet()

Creates a new empty relation set.

---

#### public AccessibleRelationSet​(
AccessibleRelation
[] relations)

Creates a new relation with the initial set of relations contained in the
array of relations passed in. Duplicate entries are ignored.

**Parameters:**
- relations

- an array of

AccessibleRelation

describing the
relation set

---

### Method Details

#### public boolean add​(
AccessibleRelation
relation)

Adds a new relation to the current relation set. If the relation is
already in the relation set, the target(s) of the specified relation is
merged with the target(s) of the existing relation. Otherwise, the new
relation is added to the relation set.

**Parameters:**
- relation

- the relation to add to the relation set

**Returns:**
- true

if relation is added to the relation set;

false

if the relation set is unchanged

---

#### public void addAll​(
AccessibleRelation
[] relations)

Adds all of the relations to the existing relation set. Duplicate entries
are ignored.

**Parameters:**
- relations

-

AccessibleRelation

array describing the
relation set

---

#### public boolean remove​(
AccessibleRelation
relation)

Removes a relation from the current relation set. If the relation is not
in the set, the relation set will be unchanged and the return value will
be

false

. If the relation is in the relation set, it will be
removed from the set and the return value will be

true

.

**Parameters:**
- relation

- the relation to remove from the relation set

**Returns:**
- true

if the relation is in the relation set;

false

if the relation set is unchanged

---

#### public void clear()

Removes all the relations from the current relation set.

---

#### public int size()

Returns the number of relations in the relation set.

**Returns:**
- the number of relations in the relation set

---

#### public boolean contains​(
String
key)

Returns whether the relation set contains a relation that matches the
specified key.

**Parameters:**
- key

- the

AccessibleRelation

key

**Returns:**
- true

if the relation is in the relation set; otherwise

false

---

#### public
AccessibleRelation
get​(
String
key)

Returns the relation that matches the specified key.

**Parameters:**
- key

- the

AccessibleRelation

key

**Returns:**
- the relation, if one exists, that matches the specified key.
Otherwise,

null

is returned.

---

#### public
AccessibleRelation
[] toArray()

Returns the current relation set as an array of

AccessibleRelation

.

**Returns:**
- AccessibleRelation

array contacting the current relation

---

#### public
String
toString()

Creates a localized string representing all the relations in the set
using the default locale.

**Overrides:**
- toString

in class

Object

**Returns:**
- comma separated localized string

**See Also:**
- AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

### Additional Sections

#### Class AccessibleRelationSet

java.lang.Object

- javax.accessibility.AccessibleRelationSet

javax.accessibility.AccessibleRelationSet

```java
public class
AccessibleRelationSet

extends
Object
```

Class

AccessibleRelationSet

determines a component's relation set.
The relation set of a component is a set of

AccessibleRelation

objects that describe the component's relationships with other components.

**Since:** 1.3
**See Also:** AccessibleRelation

public class

AccessibleRelationSet

extends

Object

Class

AccessibleRelationSet

determines a component's relation set.
The relation set of a component is a set of

AccessibleRelation

objects that describe the component's relationships with other components.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

AccessibleRelation

>

relations

Each entry in the

Vector

represents an

AccessibleRelation

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleRelationSet

()

Creates a new empty relation set.

AccessibleRelationSet

​(

AccessibleRelation

[] relations)

Creates a new relation with the initial set of relations contained in the
array of relations passed in.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

AccessibleRelation

relation)

Adds a new relation to the current relation set.

void

addAll

​(

AccessibleRelation

[] relations)

Adds all of the relations to the existing relation set.

void

clear

()

Removes all the relations from the current relation set.

boolean

contains

​(

String

key)

Returns whether the relation set contains a relation that matches the
specified key.

AccessibleRelation

get

​(

String

key)

Returns the relation that matches the specified key.

boolean

remove

​(

AccessibleRelation

relation)

Removes a relation from the current relation set.

int

size

()

Returns the number of relations in the relation set.

AccessibleRelation

[]

toArray

()

Returns the current relation set as an array of

AccessibleRelation

.

String

toString

()

Creates a localized string representing all the relations in the set
using the default locale.

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected

Vector

<

AccessibleRelation

>

relations

Each entry in the

Vector

represents an

AccessibleRelation

.

---

#### Field Summary

Each entry in the

Vector

represents an

AccessibleRelation

.

Constructor Summary

Constructors

Constructor

Description

AccessibleRelationSet

()

Creates a new empty relation set.

AccessibleRelationSet

​(

AccessibleRelation

[] relations)

Creates a new relation with the initial set of relations contained in the
array of relations passed in.

---

#### Constructor Summary

Creates a new empty relation set.

Creates a new relation with the initial set of relations contained in the
array of relations passed in.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

add

​(

AccessibleRelation

relation)

Adds a new relation to the current relation set.

void

addAll

​(

AccessibleRelation

[] relations)

Adds all of the relations to the existing relation set.

void

clear

()

Removes all the relations from the current relation set.

boolean

contains

​(

String

key)

Returns whether the relation set contains a relation that matches the
specified key.

AccessibleRelation

get

​(

String

key)

Returns the relation that matches the specified key.

boolean

remove

​(

AccessibleRelation

relation)

Removes a relation from the current relation set.

int

size

()

Returns the number of relations in the relation set.

AccessibleRelation

[]

toArray

()

Returns the current relation set as an array of

AccessibleRelation

.

String

toString

()

Creates a localized string representing all the relations in the set
using the default locale.

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

wait

,

wait

,

wait

---

#### Method Summary

Adds a new relation to the current relation set.

Adds all of the relations to the existing relation set.

Removes all the relations from the current relation set.

Returns whether the relation set contains a relation that matches the
specified key.

Returns the relation that matches the specified key.

Removes a relation from the current relation set.

Returns the number of relations in the relation set.

Returns the current relation set as an array of

AccessibleRelation

.

Creates a localized string representing all the relations in the set
using the default locale.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- relations

```java
protected
Vector
<
AccessibleRelation
> relations
```

Each entry in the

Vector

represents an

AccessibleRelation

.

**See Also:** add(javax.accessibility.AccessibleRelation)

,

addAll(javax.accessibility.AccessibleRelation[])

,

remove(javax.accessibility.AccessibleRelation)

,

contains(java.lang.String)

,

get(java.lang.String)

,

size()

,

toArray()

,

clear()

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleRelationSet

```java
public AccessibleRelationSet()
```

Creates a new empty relation set.

- AccessibleRelationSet

```java
public AccessibleRelationSet​(
AccessibleRelation
[] relations)
```

Creates a new relation with the initial set of relations contained in the
array of relations passed in. Duplicate entries are ignored.

**Parameters:** relations

- an array of

AccessibleRelation

describing the
relation set

============ METHOD DETAIL ==========

- Method Detail

- add

```java
public boolean add​(
AccessibleRelation
relation)
```

Adds a new relation to the current relation set. If the relation is
already in the relation set, the target(s) of the specified relation is
merged with the target(s) of the existing relation. Otherwise, the new
relation is added to the relation set.

**Parameters:** relation

- the relation to add to the relation set
**Returns:** true

if relation is added to the relation set;

false

if the relation set is unchanged

- addAll

```java
public void addAll​(
AccessibleRelation
[] relations)
```

Adds all of the relations to the existing relation set. Duplicate entries
are ignored.

**Parameters:** relations

-

AccessibleRelation

array describing the
relation set

- remove

```java
public boolean remove​(
AccessibleRelation
relation)
```

Removes a relation from the current relation set. If the relation is not
in the set, the relation set will be unchanged and the return value will
be

false

. If the relation is in the relation set, it will be
removed from the set and the return value will be

true

.

**Parameters:** relation

- the relation to remove from the relation set
**Returns:** true

if the relation is in the relation set;

false

if the relation set is unchanged

- clear

```java
public void clear()
```

Removes all the relations from the current relation set.

- size

```java
public int size()
```

Returns the number of relations in the relation set.

**Returns:** the number of relations in the relation set

- contains

```java
public boolean contains​(
String
key)
```

Returns whether the relation set contains a relation that matches the
specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** true

if the relation is in the relation set; otherwise

false

- get

```java
public
AccessibleRelation
get​(
String
key)
```

Returns the relation that matches the specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** the relation, if one exists, that matches the specified key.
Otherwise,

null

is returned.

- toArray

```java
public
AccessibleRelation
[] toArray()
```

Returns the current relation set as an array of

AccessibleRelation

.

**Returns:** AccessibleRelation

array contacting the current relation

- toString

```java
public
String
toString()
```

Creates a localized string representing all the relations in the set
using the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

Field Detail

- relations

```java
protected
Vector
<
AccessibleRelation
> relations
```

Each entry in the

Vector

represents an

AccessibleRelation

.

**See Also:** add(javax.accessibility.AccessibleRelation)

,

addAll(javax.accessibility.AccessibleRelation[])

,

remove(javax.accessibility.AccessibleRelation)

,

contains(java.lang.String)

,

get(java.lang.String)

,

size()

,

toArray()

,

clear()

---

#### Field Detail

relations

```java
protected
Vector
<
AccessibleRelation
> relations
```

Each entry in the

Vector

represents an

AccessibleRelation

.

**See Also:** add(javax.accessibility.AccessibleRelation)

,

addAll(javax.accessibility.AccessibleRelation[])

,

remove(javax.accessibility.AccessibleRelation)

,

contains(java.lang.String)

,

get(java.lang.String)

,

size()

,

toArray()

,

clear()

---

#### relations

protected

Vector

<

AccessibleRelation

> relations

Each entry in the

Vector

represents an

AccessibleRelation

.

Constructor Detail

- AccessibleRelationSet

```java
public AccessibleRelationSet()
```

Creates a new empty relation set.

- AccessibleRelationSet

```java
public AccessibleRelationSet​(
AccessibleRelation
[] relations)
```

Creates a new relation with the initial set of relations contained in the
array of relations passed in. Duplicate entries are ignored.

**Parameters:** relations

- an array of

AccessibleRelation

describing the
relation set

---

#### Constructor Detail

AccessibleRelationSet

```java
public AccessibleRelationSet()
```

Creates a new empty relation set.

---

#### AccessibleRelationSet

public AccessibleRelationSet()

Creates a new empty relation set.

AccessibleRelationSet

```java
public AccessibleRelationSet​(
AccessibleRelation
[] relations)
```

Creates a new relation with the initial set of relations contained in the
array of relations passed in. Duplicate entries are ignored.

**Parameters:** relations

- an array of

AccessibleRelation

describing the
relation set

---

#### AccessibleRelationSet

public AccessibleRelationSet​(

AccessibleRelation

[] relations)

Creates a new relation with the initial set of relations contained in the
array of relations passed in. Duplicate entries are ignored.

Method Detail

- add

```java
public boolean add​(
AccessibleRelation
relation)
```

Adds a new relation to the current relation set. If the relation is
already in the relation set, the target(s) of the specified relation is
merged with the target(s) of the existing relation. Otherwise, the new
relation is added to the relation set.

**Parameters:** relation

- the relation to add to the relation set
**Returns:** true

if relation is added to the relation set;

false

if the relation set is unchanged

- addAll

```java
public void addAll​(
AccessibleRelation
[] relations)
```

Adds all of the relations to the existing relation set. Duplicate entries
are ignored.

**Parameters:** relations

-

AccessibleRelation

array describing the
relation set

- remove

```java
public boolean remove​(
AccessibleRelation
relation)
```

Removes a relation from the current relation set. If the relation is not
in the set, the relation set will be unchanged and the return value will
be

false

. If the relation is in the relation set, it will be
removed from the set and the return value will be

true

.

**Parameters:** relation

- the relation to remove from the relation set
**Returns:** true

if the relation is in the relation set;

false

if the relation set is unchanged

- clear

```java
public void clear()
```

Removes all the relations from the current relation set.

- size

```java
public int size()
```

Returns the number of relations in the relation set.

**Returns:** the number of relations in the relation set

- contains

```java
public boolean contains​(
String
key)
```

Returns whether the relation set contains a relation that matches the
specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** true

if the relation is in the relation set; otherwise

false

- get

```java
public
AccessibleRelation
get​(
String
key)
```

Returns the relation that matches the specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** the relation, if one exists, that matches the specified key.
Otherwise,

null

is returned.

- toArray

```java
public
AccessibleRelation
[] toArray()
```

Returns the current relation set as an array of

AccessibleRelation

.

**Returns:** AccessibleRelation

array contacting the current relation

- toString

```java
public
String
toString()
```

Creates a localized string representing all the relations in the set
using the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### Method Detail

add

```java
public boolean add​(
AccessibleRelation
relation)
```

Adds a new relation to the current relation set. If the relation is
already in the relation set, the target(s) of the specified relation is
merged with the target(s) of the existing relation. Otherwise, the new
relation is added to the relation set.

**Parameters:** relation

- the relation to add to the relation set
**Returns:** true

if relation is added to the relation set;

false

if the relation set is unchanged

---

#### add

public boolean add​(

AccessibleRelation

relation)

Adds a new relation to the current relation set. If the relation is
already in the relation set, the target(s) of the specified relation is
merged with the target(s) of the existing relation. Otherwise, the new
relation is added to the relation set.

addAll

```java
public void addAll​(
AccessibleRelation
[] relations)
```

Adds all of the relations to the existing relation set. Duplicate entries
are ignored.

**Parameters:** relations

-

AccessibleRelation

array describing the
relation set

---

#### addAll

public void addAll​(

AccessibleRelation

[] relations)

Adds all of the relations to the existing relation set. Duplicate entries
are ignored.

remove

```java
public boolean remove​(
AccessibleRelation
relation)
```

Removes a relation from the current relation set. If the relation is not
in the set, the relation set will be unchanged and the return value will
be

false

. If the relation is in the relation set, it will be
removed from the set and the return value will be

true

.

**Parameters:** relation

- the relation to remove from the relation set
**Returns:** true

if the relation is in the relation set;

false

if the relation set is unchanged

---

#### remove

public boolean remove​(

AccessibleRelation

relation)

Removes a relation from the current relation set. If the relation is not
in the set, the relation set will be unchanged and the return value will
be

false

. If the relation is in the relation set, it will be
removed from the set and the return value will be

true

.

clear

```java
public void clear()
```

Removes all the relations from the current relation set.

---

#### clear

public void clear()

Removes all the relations from the current relation set.

size

```java
public int size()
```

Returns the number of relations in the relation set.

**Returns:** the number of relations in the relation set

---

#### size

public int size()

Returns the number of relations in the relation set.

contains

```java
public boolean contains​(
String
key)
```

Returns whether the relation set contains a relation that matches the
specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** true

if the relation is in the relation set; otherwise

false

---

#### contains

public boolean contains​(

String

key)

Returns whether the relation set contains a relation that matches the
specified key.

get

```java
public
AccessibleRelation
get​(
String
key)
```

Returns the relation that matches the specified key.

**Parameters:** key

- the

AccessibleRelation

key
**Returns:** the relation, if one exists, that matches the specified key.
Otherwise,

null

is returned.

---

#### get

public

AccessibleRelation

get​(

String

key)

Returns the relation that matches the specified key.

toArray

```java
public
AccessibleRelation
[] toArray()
```

Returns the current relation set as an array of

AccessibleRelation

.

**Returns:** AccessibleRelation

array contacting the current relation

---

#### toArray

public

AccessibleRelation

[] toArray()

Returns the current relation set as an array of

AccessibleRelation

.

toString

```java
public
String
toString()
```

Creates a localized string representing all the relations in the set
using the default locale.

**Overrides:** toString

in class

Object
**Returns:** comma separated localized string
**See Also:** AccessibleBundle.toDisplayString(java.lang.String, java.util.Locale)

---

#### toString

public

String

toString()

Creates a localized string representing all the relations in the set
using the default locale.

---

