# Class SortKey

**Source:** `java.naming\javax\naming\ldap\SortKey.html`

### Class Description

```java
public class
SortKey

extends
Object
```

A sort key and its associated sort parameters.
This class implements a sort key which is used by the LDAPv3
Control for server-side sorting of search results as defined in

RFC 2891

.

**Since:** 1.5
**See Also:** SortControl

---

### Field Details

*No entries found.*

### Constructor Details

#### public SortKey​(
String
attrID)

Creates the default sort key for an attribute. Entries will be sorted
according to the specified attribute in ascending order using the
ordering matching rule defined for use with that attribute.

**Parameters:**
- attrID

- The non-null ID of the attribute to be used as a sort
key.

---

#### public SortKey​(
String
attrID,
boolean ascendingOrder,

String
matchingRuleID)

Creates a sort key for an attribute. Entries will be sorted according to
the specified attribute in the specified sort order and using the
specified matching rule, if supplied.

**Parameters:**
- attrID

- The non-null ID of the attribute to be used as
a sort key.
- ascendingOrder

- If true then entries are arranged in ascending
order. Otherwise there are arranged in
descending order.
- matchingRuleID

- The possibly null ID of the matching rule to
use to order the attribute values. If not
specified then the ordering matching rule
defined for the sort key attribute is used.

---

### Method Details

#### public
String
getAttributeID()

Retrieves the attribute ID of the sort key.

**Returns:**
- The non-null Attribute ID of the sort key.

---

#### public boolean isAscending()

Determines the sort order.

**Returns:**
- true if the sort order is ascending, false if descending.

---

#### public
String
getMatchingRuleID()

Retrieves the matching rule ID used to order the attribute values.

**Returns:**
- The possibly null matching rule ID. If null then the
ordering matching rule defined for the sort key attribute
is used.

---

### Additional Sections

#### Class SortKey

java.lang.Object

- javax.naming.ldap.SortKey

javax.naming.ldap.SortKey

```java
public class
SortKey

extends
Object
```

A sort key and its associated sort parameters.
This class implements a sort key which is used by the LDAPv3
Control for server-side sorting of search results as defined in

RFC 2891

.

**Since:** 1.5
**See Also:** SortControl

public class

SortKey

extends

Object

A sort key and its associated sort parameters.
This class implements a sort key which is used by the LDAPv3
Control for server-side sorting of search results as defined in

RFC 2891

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SortKey

​(

String

attrID)

Creates the default sort key for an attribute.

SortKey

​(

String

attrID,
boolean ascendingOrder,

String

matchingRuleID)

Creates a sort key for an attribute.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeID

()

Retrieves the attribute ID of the sort key.

String

getMatchingRuleID

()

Retrieves the matching rule ID used to order the attribute values.

boolean

isAscending

()

Determines the sort order.

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

Constructor

Description

SortKey

​(

String

attrID)

Creates the default sort key for an attribute.

SortKey

​(

String

attrID,
boolean ascendingOrder,

String

matchingRuleID)

Creates a sort key for an attribute.

---

#### Constructor Summary

Creates the default sort key for an attribute.

Creates a sort key for an attribute.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeID

()

Retrieves the attribute ID of the sort key.

String

getMatchingRuleID

()

Retrieves the matching rule ID used to order the attribute values.

boolean

isAscending

()

Determines the sort order.

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

Retrieves the attribute ID of the sort key.

Retrieves the matching rule ID used to order the attribute values.

Determines the sort order.

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

- SortKey

```java
public SortKey​(
String
attrID)
```

Creates the default sort key for an attribute. Entries will be sorted
according to the specified attribute in ascending order using the
ordering matching rule defined for use with that attribute.

**Parameters:** attrID

- The non-null ID of the attribute to be used as a sort
key.

- SortKey

```java
public SortKey​(
String
attrID,
boolean ascendingOrder,

String
matchingRuleID)
```

Creates a sort key for an attribute. Entries will be sorted according to
the specified attribute in the specified sort order and using the
specified matching rule, if supplied.

**Parameters:** attrID

- The non-null ID of the attribute to be used as
a sort key.
**Parameters:** ascendingOrder

- If true then entries are arranged in ascending
order. Otherwise there are arranged in
descending order.
**Parameters:** matchingRuleID

- The possibly null ID of the matching rule to
use to order the attribute values. If not
specified then the ordering matching rule
defined for the sort key attribute is used.

============ METHOD DETAIL ==========

- Method Detail

- getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the attribute ID of the sort key.

**Returns:** The non-null Attribute ID of the sort key.

- isAscending

```java
public boolean isAscending()
```

Determines the sort order.

**Returns:** true if the sort order is ascending, false if descending.

- getMatchingRuleID

```java
public
String
getMatchingRuleID()
```

Retrieves the matching rule ID used to order the attribute values.

**Returns:** The possibly null matching rule ID. If null then the
ordering matching rule defined for the sort key attribute
is used.

Constructor Detail

- SortKey

```java
public SortKey​(
String
attrID)
```

Creates the default sort key for an attribute. Entries will be sorted
according to the specified attribute in ascending order using the
ordering matching rule defined for use with that attribute.

**Parameters:** attrID

- The non-null ID of the attribute to be used as a sort
key.

- SortKey

```java
public SortKey​(
String
attrID,
boolean ascendingOrder,

String
matchingRuleID)
```

Creates a sort key for an attribute. Entries will be sorted according to
the specified attribute in the specified sort order and using the
specified matching rule, if supplied.

**Parameters:** attrID

- The non-null ID of the attribute to be used as
a sort key.
**Parameters:** ascendingOrder

- If true then entries are arranged in ascending
order. Otherwise there are arranged in
descending order.
**Parameters:** matchingRuleID

- The possibly null ID of the matching rule to
use to order the attribute values. If not
specified then the ordering matching rule
defined for the sort key attribute is used.

---

#### Constructor Detail

SortKey

```java
public SortKey​(
String
attrID)
```

Creates the default sort key for an attribute. Entries will be sorted
according to the specified attribute in ascending order using the
ordering matching rule defined for use with that attribute.

**Parameters:** attrID

- The non-null ID of the attribute to be used as a sort
key.

---

#### SortKey

public SortKey​(

String

attrID)

Creates the default sort key for an attribute. Entries will be sorted
according to the specified attribute in ascending order using the
ordering matching rule defined for use with that attribute.

SortKey

```java
public SortKey​(
String
attrID,
boolean ascendingOrder,

String
matchingRuleID)
```

Creates a sort key for an attribute. Entries will be sorted according to
the specified attribute in the specified sort order and using the
specified matching rule, if supplied.

**Parameters:** attrID

- The non-null ID of the attribute to be used as
a sort key.
**Parameters:** ascendingOrder

- If true then entries are arranged in ascending
order. Otherwise there are arranged in
descending order.
**Parameters:** matchingRuleID

- The possibly null ID of the matching rule to
use to order the attribute values. If not
specified then the ordering matching rule
defined for the sort key attribute is used.

---

#### SortKey

public SortKey​(

String

attrID,
boolean ascendingOrder,

String

matchingRuleID)

Creates a sort key for an attribute. Entries will be sorted according to
the specified attribute in the specified sort order and using the
specified matching rule, if supplied.

Method Detail

- getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the attribute ID of the sort key.

**Returns:** The non-null Attribute ID of the sort key.

- isAscending

```java
public boolean isAscending()
```

Determines the sort order.

**Returns:** true if the sort order is ascending, false if descending.

- getMatchingRuleID

```java
public
String
getMatchingRuleID()
```

Retrieves the matching rule ID used to order the attribute values.

**Returns:** The possibly null matching rule ID. If null then the
ordering matching rule defined for the sort key attribute
is used.

---

#### Method Detail

getAttributeID

```java
public
String
getAttributeID()
```

Retrieves the attribute ID of the sort key.

**Returns:** The non-null Attribute ID of the sort key.

---

#### getAttributeID

public

String

getAttributeID()

Retrieves the attribute ID of the sort key.

isAscending

```java
public boolean isAscending()
```

Determines the sort order.

**Returns:** true if the sort order is ascending, false if descending.

---

#### isAscending

public boolean isAscending()

Determines the sort order.

getMatchingRuleID

```java
public
String
getMatchingRuleID()
```

Retrieves the matching rule ID used to order the attribute values.

**Returns:** The possibly null matching rule ID. If null then the
ordering matching rule defined for the sort key attribute
is used.

---

#### getMatchingRuleID

public

String

getMatchingRuleID()

Retrieves the matching rule ID used to order the attribute values.

---

