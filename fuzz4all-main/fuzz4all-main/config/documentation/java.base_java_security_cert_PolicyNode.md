# Interface PolicyNode

**Source:** `java.base\java\security\cert\PolicyNode.html`

### Class Description

```java
public interface
PolicyNode
```

An immutable valid policy tree node as defined by the PKIX certification
path validation algorithm.

One of the outputs of the PKIX certification path validation
algorithm is a valid policy tree, which includes the policies that
were determined to be valid, how this determination was reached,
and any policy qualifiers encountered. This tree is of depth

n

, where

n

is the length of the certification
path that has been validated.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However,
the valid policy tree is available for more sophisticated applications,
especially those that process policy qualifiers.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### PolicyNode
getParent()

Returns the parent of this node, or

null

if this is the
root node.

**Returns:**
- the parent of this node, or

null

if this is the
root node

---

#### Iterator
<? extends
PolicyNode
> getChildren()

Returns an iterator over the children of this node. Any attempts to
modify the children of this node through the

Iterator

's remove method must throw an

UnsupportedOperationException

.

**Returns:**
- an iterator over the children of this node

---

#### int getDepth()

Returns the depth of this node in the valid policy tree.

**Returns:**
- the depth of this node (0 for the root node, 1 for its
children, and so on)

---

#### String
getValidPolicy()

Returns the valid policy represented by this node.

**Returns:**
- the

String

OID of the valid policy
represented by this node. For the root node, this method always returns
the special anyPolicy OID: "2.5.29.32.0".

---

#### Set
<? extends
PolicyQualifierInfo
> getPolicyQualifiers()

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

**Returns:**
- an immutable

Set

of

PolicyQualifierInfo

s. For the root node, this
is always an empty

Set

.

---

#### Set
<
String
> getExpectedPolicies()

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

**Returns:**
- an immutable

Set

of expected policy

String

OIDs. For the root node, this method
always returns a

Set

with one element, the
special anyPolicy OID: "2.5.29.32.0".

---

#### boolean isCritical()

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

**Returns:**
- true

if extension marked critical,

false

otherwise. For the root node,

false

is always returned.

---

### Additional Sections

#### Interface PolicyNode

```java
public interface
PolicyNode
```

An immutable valid policy tree node as defined by the PKIX certification
path validation algorithm.

One of the outputs of the PKIX certification path validation
algorithm is a valid policy tree, which includes the policies that
were determined to be valid, how this determination was reached,
and any policy qualifiers encountered. This tree is of depth

n

, where

n

is the length of the certification
path that has been validated.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However,
the valid policy tree is available for more sophisticated applications,
especially those that process policy qualifiers.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

**Since:** 1.4

public interface

PolicyNode

An immutable valid policy tree node as defined by the PKIX certification
path validation algorithm.

One of the outputs of the PKIX certification path validation
algorithm is a valid policy tree, which includes the policies that
were determined to be valid, how this determination was reached,
and any policy qualifiers encountered. This tree is of depth

n

, where

n

is the length of the certification
path that has been validated.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However,
the valid policy tree is available for more sophisticated applications,
especially those that process policy qualifiers.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

One of the outputs of the PKIX certification path validation
algorithm is a valid policy tree, which includes the policies that
were determined to be valid, how this determination was reached,
and any policy qualifiers encountered. This tree is of depth

n

, where

n

is the length of the certification
path that has been validated.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However,
the valid policy tree is available for more sophisticated applications,
especially those that process policy qualifiers.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

Most applications will not need to examine the valid policy tree.
They can achieve their policy processing goals by setting the
policy-related parameters in

PKIXParameters

. However,
the valid policy tree is available for more sophisticated applications,
especially those that process policy qualifiers.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

PKIXCertPathValidatorResult.getPolicyTree

returns the root node of the
valid policy tree. The tree can be traversed using the

getChildren

and

getParent

methods.
Data about a particular node can be retrieved using other methods of

PolicyNode

.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

Concurrent Access

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

All

PolicyNode

objects must be immutable and
thread-safe. Multiple threads may concurrently invoke the methods defined
in this class on a single

PolicyNode

object (or more than one)
with no ill effects. This stipulation applies to all public fields and
methods of this class and any added or overridden by subclasses.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<? extends

PolicyNode

>

getChildren

()

Returns an iterator over the children of this node.

int

getDepth

()

Returns the depth of this node in the valid policy tree.

Set

<

String

>

getExpectedPolicies

()

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

PolicyNode

getParent

()

Returns the parent of this node, or

null

if this is the
root node.

Set

<? extends

PolicyQualifierInfo

>

getPolicyQualifiers

()

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

String

getValidPolicy

()

Returns the valid policy represented by this node.

boolean

isCritical

()

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Iterator

<? extends

PolicyNode

>

getChildren

()

Returns an iterator over the children of this node.

int

getDepth

()

Returns the depth of this node in the valid policy tree.

Set

<

String

>

getExpectedPolicies

()

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

PolicyNode

getParent

()

Returns the parent of this node, or

null

if this is the
root node.

Set

<? extends

PolicyQualifierInfo

>

getPolicyQualifiers

()

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

String

getValidPolicy

()

Returns the valid policy represented by this node.

boolean

isCritical

()

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

---

#### Method Summary

Returns an iterator over the children of this node.

Returns the depth of this node in the valid policy tree.

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

Returns the parent of this node, or

null

if this is the
root node.

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

Returns the valid policy represented by this node.

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

============ METHOD DETAIL ==========

- Method Detail

- getParent

```java
PolicyNode
getParent()
```

Returns the parent of this node, or

null

if this is the
root node.

**Returns:** the parent of this node, or

null

if this is the
root node

- getChildren

```java
Iterator
<? extends
PolicyNode
> getChildren()
```

Returns an iterator over the children of this node. Any attempts to
modify the children of this node through the

Iterator

's remove method must throw an

UnsupportedOperationException

.

**Returns:** an iterator over the children of this node

- getDepth

```java
int getDepth()
```

Returns the depth of this node in the valid policy tree.

**Returns:** the depth of this node (0 for the root node, 1 for its
children, and so on)

- getValidPolicy

```java
String
getValidPolicy()
```

Returns the valid policy represented by this node.

**Returns:** the

String

OID of the valid policy
represented by this node. For the root node, this method always returns
the special anyPolicy OID: "2.5.29.32.0".

- getPolicyQualifiers

```java
Set
<? extends
PolicyQualifierInfo
> getPolicyQualifiers()
```

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

**Returns:** an immutable

Set

of

PolicyQualifierInfo

s. For the root node, this
is always an empty

Set

.

- getExpectedPolicies

```java
Set
<
String
> getExpectedPolicies()
```

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

**Returns:** an immutable

Set

of expected policy

String

OIDs. For the root node, this method
always returns a

Set

with one element, the
special anyPolicy OID: "2.5.29.32.0".

- isCritical

```java
boolean isCritical()
```

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

**Returns:** true

if extension marked critical,

false

otherwise. For the root node,

false

is always returned.

Method Detail

- getParent

```java
PolicyNode
getParent()
```

Returns the parent of this node, or

null

if this is the
root node.

**Returns:** the parent of this node, or

null

if this is the
root node

- getChildren

```java
Iterator
<? extends
PolicyNode
> getChildren()
```

Returns an iterator over the children of this node. Any attempts to
modify the children of this node through the

Iterator

's remove method must throw an

UnsupportedOperationException

.

**Returns:** an iterator over the children of this node

- getDepth

```java
int getDepth()
```

Returns the depth of this node in the valid policy tree.

**Returns:** the depth of this node (0 for the root node, 1 for its
children, and so on)

- getValidPolicy

```java
String
getValidPolicy()
```

Returns the valid policy represented by this node.

**Returns:** the

String

OID of the valid policy
represented by this node. For the root node, this method always returns
the special anyPolicy OID: "2.5.29.32.0".

- getPolicyQualifiers

```java
Set
<? extends
PolicyQualifierInfo
> getPolicyQualifiers()
```

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

**Returns:** an immutable

Set

of

PolicyQualifierInfo

s. For the root node, this
is always an empty

Set

.

- getExpectedPolicies

```java
Set
<
String
> getExpectedPolicies()
```

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

**Returns:** an immutable

Set

of expected policy

String

OIDs. For the root node, this method
always returns a

Set

with one element, the
special anyPolicy OID: "2.5.29.32.0".

- isCritical

```java
boolean isCritical()
```

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

**Returns:** true

if extension marked critical,

false

otherwise. For the root node,

false

is always returned.

---

#### Method Detail

getParent

```java
PolicyNode
getParent()
```

Returns the parent of this node, or

null

if this is the
root node.

**Returns:** the parent of this node, or

null

if this is the
root node

---

#### getParent

PolicyNode

getParent()

Returns the parent of this node, or

null

if this is the
root node.

getChildren

```java
Iterator
<? extends
PolicyNode
> getChildren()
```

Returns an iterator over the children of this node. Any attempts to
modify the children of this node through the

Iterator

's remove method must throw an

UnsupportedOperationException

.

**Returns:** an iterator over the children of this node

---

#### getChildren

Iterator

<? extends

PolicyNode

> getChildren()

Returns an iterator over the children of this node. Any attempts to
modify the children of this node through the

Iterator

's remove method must throw an

UnsupportedOperationException

.

getDepth

```java
int getDepth()
```

Returns the depth of this node in the valid policy tree.

**Returns:** the depth of this node (0 for the root node, 1 for its
children, and so on)

---

#### getDepth

int getDepth()

Returns the depth of this node in the valid policy tree.

getValidPolicy

```java
String
getValidPolicy()
```

Returns the valid policy represented by this node.

**Returns:** the

String

OID of the valid policy
represented by this node. For the root node, this method always returns
the special anyPolicy OID: "2.5.29.32.0".

---

#### getValidPolicy

String

getValidPolicy()

Returns the valid policy represented by this node.

getPolicyQualifiers

```java
Set
<? extends
PolicyQualifierInfo
> getPolicyQualifiers()
```

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

**Returns:** an immutable

Set

of

PolicyQualifierInfo

s. For the root node, this
is always an empty

Set

.

---

#### getPolicyQualifiers

Set

<? extends

PolicyQualifierInfo

> getPolicyQualifiers()

Returns the set of policy qualifiers associated with the
valid policy represented by this node.

getExpectedPolicies

```java
Set
<
String
> getExpectedPolicies()
```

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

**Returns:** an immutable

Set

of expected policy

String

OIDs. For the root node, this method
always returns a

Set

with one element, the
special anyPolicy OID: "2.5.29.32.0".

---

#### getExpectedPolicies

Set

<

String

> getExpectedPolicies()

Returns the set of expected policies that would satisfy this
node's valid policy in the next certificate to be processed.

isCritical

```java
boolean isCritical()
```

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

**Returns:** true

if extension marked critical,

false

otherwise. For the root node,

false

is always returned.

---

#### isCritical

boolean isCritical()

Returns the criticality indicator of the certificate policy extension
in the most recently processed certificate.

---

