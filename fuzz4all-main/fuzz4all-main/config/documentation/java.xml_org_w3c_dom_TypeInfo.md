# Interface TypeInfo

**Source:** `java.xml\org\w3c\dom\TypeInfo.html`

### Class Description

```java
public interface
TypeInfo
```

The

TypeInfo

interface represents a type referenced from

Element

or

Attr

nodes, specified in the schemas
associated with the document. The type is a pair of a namespace URI and
name properties, and depends on the document's schema.

If the document's schema is an XML DTD [

XML 1.0

], the values
are computed as follows:

- If this type is referenced from an

Attr

node,

typeNamespace

is

"http://www.w3.org/TR/REC-xml"

and

typeName

represents the

[attribute type]

property in the [

XML Information Set

]
. If there is no declaration for the attribute,

typeNamespace

and

typeName

are

null

.
- If this type is
referenced from an

Element

node,

typeNamespace

and

typeName

are

null

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, the values are computed as follows using the post-schema-validation
infoset contributions (also called PSVI contributions):

- If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.
- If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

---

### Field Details

#### static final int DERIVATION_RESTRICTION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

The reference type definition is derived by restriction from the
other type definition if the other type definition is the same as the
reference type definition, or if the other type definition can be
reached recursively following the {base type definition} property
from the reference type definition, and all the

derivation methods

involved are restriction.

**See Also:**
- Constant Field Values

---

#### static final int DERIVATION_EXTENSION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

The reference type definition is derived by extension from the
other type definition if the other type definition can be reached
recursively following the {base type definition} property from the
reference type definition, and at least one of the

derivation methods

involved is an extension.

**See Also:**
- Constant Field Values

---

#### static final int DERIVATION_UNION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

The reference type definition is derived by union from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

union

, and one of the {member type definitions} is T2. Note that T1 could be
the same as the reference type definition, and T2 could be the same
as the other type definition.

**See Also:**
- Constant Field Values

---

#### static final int DERIVATION_LIST

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

The reference type definition is derived by list from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

list

, and T2 is the {item type definition}. Note that T1 could be the same as
the reference type definition, and T2 could be the same as the other
type definition.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getTypeName()

The name of a type declared for the associated element or attribute,
or

null

if unknown.

---

#### String
getTypeNamespace()

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

---

#### boolean isDerivedFrom​(
String
typeNamespaceArg,

String
typeNameArg,
int derivationMethod)

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

**Parameters:**
- typeNamespaceArg

- the namespace of the other type definition.
- typeNameArg

- the name of the other type definition.
- derivationMethod

- the type of derivation and conditions applied
between two types, as described in the list of constants provided
in this interface.

**Returns:**
- If the document's schema is a DTD or no schema is associated
with the document, this method will always return

false

. If the document's schema is an XML Schema, the method will return

true

if the reference type definition is derived from
the other type definition according to the derivation parameter. If
the value of the parameter is

0

(no bit is set to

1

for the

derivationMethod

parameter),
the method will return

true

if the other type
definition can be reached by recursing any combination of {base
type definition}, {item type definition}, or {member type
definitions} from the reference type definition.

---

### Additional Sections

#### Interface TypeInfo

```java
public interface
TypeInfo
```

The

TypeInfo

interface represents a type referenced from

Element

or

Attr

nodes, specified in the schemas
associated with the document. The type is a pair of a namespace URI and
name properties, and depends on the document's schema.

If the document's schema is an XML DTD [

XML 1.0

], the values
are computed as follows:

- If this type is referenced from an

Attr

node,

typeNamespace

is

"http://www.w3.org/TR/REC-xml"

and

typeName

represents the

[attribute type]

property in the [

XML Information Set

]
. If there is no declaration for the attribute,

typeNamespace

and

typeName

are

null

.
- If this type is
referenced from an

Element

node,

typeNamespace

and

typeName

are

null

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, the values are computed as follows using the post-schema-validation
infoset contributions (also called PSVI contributions):

- If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.
- If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

**Since:** 1.5, DOM Level 3

public interface

TypeInfo

The

TypeInfo

interface represents a type referenced from

Element

or

Attr

nodes, specified in the schemas
associated with the document. The type is a pair of a namespace URI and
name properties, and depends on the document's schema.

If the document's schema is an XML DTD [

XML 1.0

], the values
are computed as follows:

- If this type is referenced from an

Attr

node,

typeNamespace

is

"http://www.w3.org/TR/REC-xml"

and

typeName

represents the

[attribute type]

property in the [

XML Information Set

]
. If there is no declaration for the attribute,

typeNamespace

and

typeName

are

null

.
- If this type is
referenced from an

Element

node,

typeNamespace

and

typeName

are

null

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, the values are computed as follows using the post-schema-validation
infoset contributions (also called PSVI contributions):

- If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.
- If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

If the document's schema is an XML DTD [

XML 1.0

], the values
are computed as follows:

- If this type is referenced from an

Attr

node,

typeNamespace

is

"http://www.w3.org/TR/REC-xml"

and

typeName

represents the

[attribute type]

property in the [

XML Information Set

]
. If there is no declaration for the attribute,

typeNamespace

and

typeName

are

null

.
- If this type is
referenced from an

Element

node,

typeNamespace

and

typeName

are

null

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, the values are computed as follows using the post-schema-validation
infoset contributions (also called PSVI contributions):

- If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.
- If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

If this type is referenced from an

Attr

node,

typeNamespace

is

"http://www.w3.org/TR/REC-xml"

and

typeName

represents the

[attribute type]

property in the [

XML Information Set

]
. If there is no declaration for the attribute,

typeNamespace

and

typeName

are

null

.

If this type is
referenced from an

Element

node,

typeNamespace

and

typeName

are

null

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, the values are computed as follows using the post-schema-validation
infoset contributions (also called PSVI contributions):

- If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.
- If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

If the

[validity]

property exists AND is

"invalid"

or

"notKnown"

: the {target namespace} and {name} properties of the declared type if
available, otherwise

null

.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.

If the

[validity]

property exists and is

"valid"

:

- If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.
- If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

At the time of writing, the XML Schema specification does
not require exposing the declared type. Thus, DOM implementations might
choose not to provide type information if validity is not valid.

If

[member type definition]

exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If the

[type definition]

property exists:

- If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If the

[member type definition anonymous]

exists:

- If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If the

[type definition anonymous]

exists:

- If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;
- Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If {name} is not absent, then expose {name} and {target
namespace} properties of the

[member type definition]

property;

Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If {name} is not absent, then expose {name} and {target
namespace} properties of the

[type definition]

property;

Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If it is false, then expose

[member type definition name]

and

[member type definition namespace]

properties;

Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

If it is false, then expose

[type definition name]

and

[type definition namespace]

properties;

Otherwise, expose the namespace and local name of the
corresponding anonymous type name.

Note:

Other schema languages are outside the scope of the W3C
and therefore should define how to represent their type systems using

TypeInfo

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

See also the

Document Object Model (DOM) Level 3 Core Specification

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DERIVATION_EXTENSION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

static int

DERIVATION_LIST

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

static int

DERIVATION_RESTRICTION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

static int

DERIVATION_UNION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getTypeName

()

The name of a type declared for the associated element or attribute,
or

null

if unknown.

String

getTypeNamespace

()

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

boolean

isDerivedFrom

​(

String

typeNamespaceArg,

String

typeNameArg,
int derivationMethod)

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

Field Summary

Fields

Modifier and Type

Field

Description

static int

DERIVATION_EXTENSION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

static int

DERIVATION_LIST

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

static int

DERIVATION_RESTRICTION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

static int

DERIVATION_UNION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

---

#### Field Summary

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getTypeName

()

The name of a type declared for the associated element or attribute,
or

null

if unknown.

String

getTypeNamespace

()

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

boolean

isDerivedFrom

​(

String

typeNamespaceArg,

String

typeNameArg,
int derivationMethod)

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

---

#### Method Summary

The name of a type declared for the associated element or attribute,
or

null

if unknown.

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

============ FIELD DETAIL ===========

- Field Detail

- DERIVATION_RESTRICTION

```java
static final int DERIVATION_RESTRICTION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

The reference type definition is derived by restriction from the
other type definition if the other type definition is the same as the
reference type definition, or if the other type definition can be
reached recursively following the {base type definition} property
from the reference type definition, and all the

derivation methods

involved are restriction.

**See Also:** Constant Field Values

- DERIVATION_EXTENSION

```java
static final int DERIVATION_EXTENSION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

The reference type definition is derived by extension from the
other type definition if the other type definition can be reached
recursively following the {base type definition} property from the
reference type definition, and at least one of the

derivation methods

involved is an extension.

**See Also:** Constant Field Values

- DERIVATION_UNION

```java
static final int DERIVATION_UNION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

The reference type definition is derived by union from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

union

, and one of the {member type definitions} is T2. Note that T1 could be
the same as the reference type definition, and T2 could be the same
as the other type definition.

**See Also:** Constant Field Values

- DERIVATION_LIST

```java
static final int DERIVATION_LIST
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

The reference type definition is derived by list from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

list

, and T2 is the {item type definition}. Note that T1 could be the same as
the reference type definition, and T2 could be the same as the other
type definition.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getTypeName

```java
String
getTypeName()
```

The name of a type declared for the associated element or attribute,
or

null

if unknown.

- getTypeNamespace

```java
String
getTypeNamespace()
```

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

- isDerivedFrom

```java
boolean isDerivedFrom​(
String
typeNamespaceArg,

String
typeNameArg,
int derivationMethod)
```

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

**Parameters:** typeNamespaceArg

- the namespace of the other type definition.
**Parameters:** typeNameArg

- the name of the other type definition.
**Parameters:** derivationMethod

- the type of derivation and conditions applied
between two types, as described in the list of constants provided
in this interface.
**Returns:** If the document's schema is a DTD or no schema is associated
with the document, this method will always return

false

. If the document's schema is an XML Schema, the method will return

true

if the reference type definition is derived from
the other type definition according to the derivation parameter. If
the value of the parameter is

0

(no bit is set to

1

for the

derivationMethod

parameter),
the method will return

true

if the other type
definition can be reached by recursing any combination of {base
type definition}, {item type definition}, or {member type
definitions} from the reference type definition.

Field Detail

- DERIVATION_RESTRICTION

```java
static final int DERIVATION_RESTRICTION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

The reference type definition is derived by restriction from the
other type definition if the other type definition is the same as the
reference type definition, or if the other type definition can be
reached recursively following the {base type definition} property
from the reference type definition, and all the

derivation methods

involved are restriction.

**See Also:** Constant Field Values

- DERIVATION_EXTENSION

```java
static final int DERIVATION_EXTENSION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

The reference type definition is derived by extension from the
other type definition if the other type definition can be reached
recursively following the {base type definition} property from the
reference type definition, and at least one of the

derivation methods

involved is an extension.

**See Also:** Constant Field Values

- DERIVATION_UNION

```java
static final int DERIVATION_UNION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

The reference type definition is derived by union from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

union

, and one of the {member type definitions} is T2. Note that T1 could be
the same as the reference type definition, and T2 could be the same
as the other type definition.

**See Also:** Constant Field Values

- DERIVATION_LIST

```java
static final int DERIVATION_LIST
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

The reference type definition is derived by list from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

list

, and T2 is the {item type definition}. Note that T1 could be the same as
the reference type definition, and T2 could be the same as the other
type definition.

**See Also:** Constant Field Values

---

#### Field Detail

DERIVATION_RESTRICTION

```java
static final int DERIVATION_RESTRICTION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

The reference type definition is derived by restriction from the
other type definition if the other type definition is the same as the
reference type definition, or if the other type definition can be
reached recursively following the {base type definition} property
from the reference type definition, and all the

derivation methods

involved are restriction.

**See Also:** Constant Field Values

---

#### DERIVATION_RESTRICTION

static final int DERIVATION_RESTRICTION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

restriction

if complex types are involved, or a

restriction

if simple types are involved.

The reference type definition is derived by restriction from the
other type definition if the other type definition is the same as the
reference type definition, or if the other type definition can be
reached recursively following the {base type definition} property
from the reference type definition, and all the

derivation methods

involved are restriction.

DERIVATION_EXTENSION

```java
static final int DERIVATION_EXTENSION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

The reference type definition is derived by extension from the
other type definition if the other type definition can be reached
recursively following the {base type definition} property from the
reference type definition, and at least one of the

derivation methods

involved is an extension.

**See Also:** Constant Field Values

---

#### DERIVATION_EXTENSION

static final int DERIVATION_EXTENSION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the derivation by

extension

.

The reference type definition is derived by extension from the
other type definition if the other type definition can be reached
recursively following the {base type definition} property from the
reference type definition, and at least one of the

derivation methods

involved is an extension.

DERIVATION_UNION

```java
static final int DERIVATION_UNION
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

The reference type definition is derived by union from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

union

, and one of the {member type definitions} is T2. Note that T1 could be
the same as the reference type definition, and T2 could be the same
as the other type definition.

**See Also:** Constant Field Values

---

#### DERIVATION_UNION

static final int DERIVATION_UNION

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

union

if simple types are involved.

The reference type definition is derived by union from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

union

, and one of the {member type definitions} is T2. Note that T1 could be
the same as the reference type definition, and T2 could be the same
as the other type definition.

DERIVATION_LIST

```java
static final int DERIVATION_LIST
```

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

The reference type definition is derived by list from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

list

, and T2 is the {item type definition}. Note that T1 could be the same as
the reference type definition, and T2 could be the same as the other
type definition.

**See Also:** Constant Field Values

---

#### DERIVATION_LIST

static final int DERIVATION_LIST

If the document's schema is an XML Schema [

XML Schema Part 1

]
, this constant represents the

list

.

The reference type definition is derived by list from the other
type definition if there exists two type definitions T1 and T2 such
as the reference type definition is derived from T1 by

DERIVATION_RESTRICTION

or

DERIVATION_EXTENSION

, T2 is derived from the other type
definition by

DERIVATION_RESTRICTION

, T1 has {variety}

list

, and T2 is the {item type definition}. Note that T1 could be the same as
the reference type definition, and T2 could be the same as the other
type definition.

Method Detail

- getTypeName

```java
String
getTypeName()
```

The name of a type declared for the associated element or attribute,
or

null

if unknown.

- getTypeNamespace

```java
String
getTypeNamespace()
```

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

- isDerivedFrom

```java
boolean isDerivedFrom​(
String
typeNamespaceArg,

String
typeNameArg,
int derivationMethod)
```

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

**Parameters:** typeNamespaceArg

- the namespace of the other type definition.
**Parameters:** typeNameArg

- the name of the other type definition.
**Parameters:** derivationMethod

- the type of derivation and conditions applied
between two types, as described in the list of constants provided
in this interface.
**Returns:** If the document's schema is a DTD or no schema is associated
with the document, this method will always return

false

. If the document's schema is an XML Schema, the method will return

true

if the reference type definition is derived from
the other type definition according to the derivation parameter. If
the value of the parameter is

0

(no bit is set to

1

for the

derivationMethod

parameter),
the method will return

true

if the other type
definition can be reached by recursing any combination of {base
type definition}, {item type definition}, or {member type
definitions} from the reference type definition.

---

#### Method Detail

getTypeName

```java
String
getTypeName()
```

The name of a type declared for the associated element or attribute,
or

null

if unknown.

---

#### getTypeName

String

getTypeName()

The name of a type declared for the associated element or attribute,
or

null

if unknown.

getTypeNamespace

```java
String
getTypeNamespace()
```

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

---

#### getTypeNamespace

String

getTypeNamespace()

The namespace of the type declared for the associated element or
attribute or

null

if the element does not have
declaration or if no namespace information is available.

isDerivedFrom

```java
boolean isDerivedFrom​(
String
typeNamespaceArg,

String
typeNameArg,
int derivationMethod)
```

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

**Parameters:** typeNamespaceArg

- the namespace of the other type definition.
**Parameters:** typeNameArg

- the name of the other type definition.
**Parameters:** derivationMethod

- the type of derivation and conditions applied
between two types, as described in the list of constants provided
in this interface.
**Returns:** If the document's schema is a DTD or no schema is associated
with the document, this method will always return

false

. If the document's schema is an XML Schema, the method will return

true

if the reference type definition is derived from
the other type definition according to the derivation parameter. If
the value of the parameter is

0

(no bit is set to

1

for the

derivationMethod

parameter),
the method will return

true

if the other type
definition can be reached by recursing any combination of {base
type definition}, {item type definition}, or {member type
definitions} from the reference type definition.

---

#### isDerivedFrom

boolean isDerivedFrom​(

String

typeNamespaceArg,

String

typeNameArg,
int derivationMethod)

This method returns if there is a derivation between the reference
type definition, i.e. the

TypeInfo

on which the method
is being called, and the other type definition, i.e. the one passed
as parameters.

---

