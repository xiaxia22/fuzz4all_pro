# Class ValidatorHandler

**Source:** `java.xml\javax\xml\validation\ValidatorHandler.html`

### Class Description

```java
public abstract class
ValidatorHandler

extends
Object

implements
ContentHandler
```

Streaming validator that works on SAX stream.

A

ValidatorHandler

object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

ValidatorHandler

object is not used from
more than one thread at any given time.

ValidatorHandler

checks if the SAX events follow
the set of constraints described in the associated

Schema

,
and additionally it may modify the SAX events (for example
by adding default values, etc.)

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

**All Implemented Interfaces:** ContentHandler

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ValidatorHandler()

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

### Method Details

#### public abstract void setContentHandler​(
ContentHandler
receiver)

Sets the

ContentHandler

which receives
the augmented validation result.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

**Parameters:**
- receiver

- A

ContentHandler

or a null value.

---

#### public abstract
ContentHandler
getContentHandler()

Gets the

ContentHandler

which receives the
augmented validation result.

**Returns:**
- This method returns the object that was last set through
the

getContentHandler()

method, or null
if that method has never been called since this

ValidatorHandler

has created.

**See Also:**
- setContentHandler(ContentHandler)

---

#### public abstract void setErrorHandler​(
ErrorHandler
errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:**
- errorHandler

- A new error handler to be set. This parameter can be null.

---

#### public abstract
ErrorHandler
getErrorHandler()

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

**Returns:**
- This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

ValidatorHandler

has created.

**See Also:**
- setErrorHandler(ErrorHandler)

---

#### public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:**
- resourceResolver

- A new resource resolver to be set. This parameter can be null.

---

#### public abstract
LSResourceResolver
getResourceResolver()

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

**Returns:**
- This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

ValidatorHandler

has created.

**See Also:**
- setErrorHandler(ErrorHandler)

---

#### public abstract
TypeInfoProvider
getTypeInfoProvider()

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

**Returns:**
- null if the validator / schema language does not support
the notion of

TypeInfo

.
Otherwise a non-null valid

TypeInfoProvider

.

---

#### public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:**
- name

- The feature name, which is a non-null fully-qualified URI.

**Returns:**
- The current value of the feature (true or false).

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot determine its value at this time.
- NullPointerException

- When

name

is

null

.

**See Also:**
- setFeature(String, boolean)

---

#### public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:**
- name

- The feature name, which is a non-null fully-qualified URI.
- value

- The requested value of the feature (true or false).

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot set the requested value.
- NullPointerException

- When

name

is

null

.

**See Also:**
- getFeature(String)

---

#### public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

**Parameters:**
- name

- The property name, which is a non-null fully-qualified URI.
- object

- The requested value for the property.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

ValidatorHandler

recognizes the property name but
cannot set the requested value.
- NullPointerException

- When

name

is

null

.

---

#### public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:**
- name

- The property name, which is a non-null fully-qualified URI.

**Returns:**
- The current value of the property.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
- NullPointerException

- When

name

is

null

.

**See Also:**
- setProperty(String, Object)

---

### Additional Sections

#### Class ValidatorHandler

java.lang.Object

- javax.xml.validation.ValidatorHandler

javax.xml.validation.ValidatorHandler

**All Implemented Interfaces:** ContentHandler

```java
public abstract class
ValidatorHandler

extends
Object

implements
ContentHandler
```

Streaming validator that works on SAX stream.

A

ValidatorHandler

object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

ValidatorHandler

object is not used from
more than one thread at any given time.

ValidatorHandler

checks if the SAX events follow
the set of constraints described in the associated

Schema

,
and additionally it may modify the SAX events (for example
by adding default values, etc.)

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

**Since:** 1.5

public abstract class

ValidatorHandler

extends

Object

implements

ContentHandler

Streaming validator that works on SAX stream.

A

ValidatorHandler

object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

ValidatorHandler

object is not used from
more than one thread at any given time.

ValidatorHandler

checks if the SAX events follow
the set of constraints described in the associated

Schema

,
and additionally it may modify the SAX events (for example
by adding default values, etc.)

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

A

ValidatorHandler

object is not thread-safe and not reentrant.
In other words, it is the application's responsibility to make
sure that one

ValidatorHandler

object is not used from
more than one thread at any given time.

ValidatorHandler

checks if the SAX events follow
the set of constraints described in the associated

Schema

,
and additionally it may modify the SAX events (for example
by adding default values, etc.)

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

ValidatorHandler

checks if the SAX events follow
the set of constraints described in the associated

Schema

,
and additionally it may modify the SAX events (for example
by adding default values, etc.)

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

ValidatorHandler

extends from

ContentHandler

,
but it refines the underlying

ContentHandler

in
the following way:

- startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

startElement/endElement events must receive non-null String
for

uri

,

localName

, and

qname

,
even though SAX allows some of them to be null.
Similarly, the user-specified

ContentHandler

will receive non-null
Strings for all three parameters.

Applications must ensure that

ValidatorHandler

's

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

are invoked
properly. Similarly, the user-specified

ContentHandler

will receive startPrefixMapping/endPrefixMapping events.
If the

ValidatorHandler

introduces additional namespace
bindings, the user-specified

ContentHandler

will receive
additional startPrefixMapping/endPrefixMapping events.

Attributes

for the

ContentHandler.startElement(String,String,String,Attributes)

method
may or may not include xmlns* attributes.

A

ValidatorHandler

is automatically reset every time
the startDocument method is invoked.

Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

---

#### Recognized Properties and Features

This spec defines the following feature that must be recognized
by all

ValidatorHandler

implementations.

http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

---

#### http://xml.org/sax/features/namespace-prefixes

This feature controls how a

ValidatorHandler

introduces
namespace bindings that were not present in the original SAX event
stream.
When this feature is set to true, it must make
sure that the user's

ContentHandler

will see
the corresponding

xmlns*

attribute in
the

Attributes

object of the

ContentHandler.startElement(String,String,String,Attributes)

callback. Otherwise,

xmlns*

attributes must not be
added to

Attributes

that's passed to the
user-specified

ContentHandler

.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

(Note that regardless of this switch, namespace bindings are
always notified to applications through

ContentHandler.startPrefixMapping(String,String)

and

ContentHandler.endPrefixMapping(String)

methods of the

ContentHandler

specified by the user.)

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

Note that this feature does

NOT

affect the way
a

ValidatorHandler

receives SAX events. It merely
changes the way it augments SAX events.

This feature is set to

false

by default.

This feature is set to

false

by default.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ValidatorHandler

()

Constructor for derived classes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

ContentHandler

getContentHandler

()

Gets the

ContentHandler

which receives the
augmented validation result.

abstract

ErrorHandler

getErrorHandler

()

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

boolean

getFeature

​(

String

name)

Look up the value of a feature flag.

Object

getProperty

​(

String

name)

Look up the value of a property.

abstract

LSResourceResolver

getResourceResolver

()

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

abstract

TypeInfoProvider

getTypeInfoProvider

()

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

abstract void

setContentHandler

​(

ContentHandler

receiver)

Sets the

ContentHandler

which receives
the augmented validation result.

abstract void

setErrorHandler

​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the validation.

void

setFeature

​(

String

name,
boolean value)

Set a feature for this

ValidatorHandler

.

void

setProperty

​(

String

name,

Object

object)

Set the value of a property.

abstract void

setResourceResolver

​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

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

- Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ValidatorHandler

()

Constructor for derived classes.

---

#### Constructor Summary

Constructor for derived classes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

ContentHandler

getContentHandler

()

Gets the

ContentHandler

which receives the
augmented validation result.

abstract

ErrorHandler

getErrorHandler

()

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

boolean

getFeature

​(

String

name)

Look up the value of a feature flag.

Object

getProperty

​(

String

name)

Look up the value of a property.

abstract

LSResourceResolver

getResourceResolver

()

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

abstract

TypeInfoProvider

getTypeInfoProvider

()

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

abstract void

setContentHandler

​(

ContentHandler

receiver)

Sets the

ContentHandler

which receives
the augmented validation result.

abstract void

setErrorHandler

​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the validation.

void

setFeature

​(

String

name,
boolean value)

Set a feature for this

ValidatorHandler

.

void

setProperty

​(

String

name,

Object

object)

Set the value of a property.

abstract void

setResourceResolver

​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

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

- Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

---

#### Method Summary

Gets the

ContentHandler

which receives the
augmented validation result.

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

Look up the value of a feature flag.

Look up the value of a property.

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

Sets the

ContentHandler

which receives
the augmented validation result.

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Set a feature for this

ValidatorHandler

.

Set the value of a property.

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

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

Methods declared in interface org.xml.sax.

ContentHandler

characters

,

endDocument

,

endElement

,

endPrefixMapping

,

ignorableWhitespace

,

processingInstruction

,

setDocumentLocator

,

skippedEntity

,

startDocument

,

startElement

,

startPrefixMapping

---

#### Methods declared in interface org.xml.sax. ContentHandler

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ValidatorHandler

```java
protected ValidatorHandler()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

============ METHOD DETAIL ==========

- Method Detail

- setContentHandler

```java
public abstract void setContentHandler​(
ContentHandler
receiver)
```

Sets the

ContentHandler

which receives
the augmented validation result.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

**Parameters:** receiver

- A

ContentHandler

or a null value.

- getContentHandler

```java
public abstract
ContentHandler
getContentHandler()
```

Gets the

ContentHandler

which receives the
augmented validation result.

**Returns:** This method returns the object that was last set through
the

getContentHandler()

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setContentHandler(ContentHandler)

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** errorHandler

- A new error handler to be set. This parameter can be null.

- getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

- setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

- getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

- getTypeInfoProvider

```java
public abstract
TypeInfoProvider
getTypeInfoProvider()
```

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

**Returns:** null if the validator / schema language does not support
the notion of

TypeInfo

.
Otherwise a non-null valid

TypeInfoProvider

.

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setFeature(String, boolean)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** getFeature(String)

- setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setProperty(String, Object)

Constructor Detail

- ValidatorHandler

```java
protected ValidatorHandler()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

#### Constructor Detail

ValidatorHandler

```java
protected ValidatorHandler()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

#### ValidatorHandler

protected ValidatorHandler()

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

ValidatorHandler

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

Method Detail

- setContentHandler

```java
public abstract void setContentHandler​(
ContentHandler
receiver)
```

Sets the

ContentHandler

which receives
the augmented validation result.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

**Parameters:** receiver

- A

ContentHandler

or a null value.

- getContentHandler

```java
public abstract
ContentHandler
getContentHandler()
```

Gets the

ContentHandler

which receives the
augmented validation result.

**Returns:** This method returns the object that was last set through
the

getContentHandler()

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setContentHandler(ContentHandler)

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** errorHandler

- A new error handler to be set. This parameter can be null.

- getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

- setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

- getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

- getTypeInfoProvider

```java
public abstract
TypeInfoProvider
getTypeInfoProvider()
```

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

**Returns:** null if the validator / schema language does not support
the notion of

TypeInfo

.
Otherwise a non-null valid

TypeInfoProvider

.

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setFeature(String, boolean)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** getFeature(String)

- setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setProperty(String, Object)

---

#### Method Detail

setContentHandler

```java
public abstract void setContentHandler​(
ContentHandler
receiver)
```

Sets the

ContentHandler

which receives
the augmented validation result.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

**Parameters:** receiver

- A

ContentHandler

or a null value.

---

#### setContentHandler

public abstract void setContentHandler​(

ContentHandler

receiver)

Sets the

ContentHandler

which receives
the augmented validation result.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

When a

ContentHandler

is specified, a

ValidatorHandler

will work as a filter
and basically copy the incoming events to the
specified

ContentHandler

.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

In doing so, a

ValidatorHandler

may modify
the events, for example by adding defaulted attributes.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

A

ValidatorHandler

may buffer events to certain
extent, but to allow

ValidatorHandler

to be used
by a parser, the following requirement has to be met.

- When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

When

ContentHandler.startElement(String, String, String, Attributes)

,

ContentHandler.endElement(String, String, String)

,

ContentHandler.startDocument()

, or

ContentHandler.endDocument()

are invoked on a

ValidatorHandler

,
the same method on the user-specified

ContentHandler

must be invoked for the same event before the callback
returns.

ValidatorHandler

may not introduce new elements that
were not present in the input.

ValidatorHandler

may not remove attributes that were
present in the input.

When a callback method on the specified

ContentHandler

throws an exception, the same exception object must be thrown
from the

ValidatorHandler

. The

ErrorHandler

should not be notified of such an exception.

This method can be called even during a middle of a validation.

This method can be called even during a middle of a validation.

getContentHandler

```java
public abstract
ContentHandler
getContentHandler()
```

Gets the

ContentHandler

which receives the
augmented validation result.

**Returns:** This method returns the object that was last set through
the

getContentHandler()

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setContentHandler(ContentHandler)

---

#### getContentHandler

public abstract

ContentHandler

getContentHandler()

Gets the

ContentHandler

which receives the
augmented validation result.

setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** errorHandler

- A new error handler to be set. This parameter can be null.

---

#### setErrorHandler

public abstract void setErrorHandler​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the validation.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

Error handler can be used to customize the error handling process
during a validation. When an

ErrorHandler

is set,
errors found during the validation will be first sent
to the

ErrorHandler

.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

The error handler can abort further validation immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
validation by returning normally from the

ErrorHandler

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

If any

Throwable

is thrown from an

ErrorHandler

,
the same

Throwable

object will be thrown toward the
root of the call stack.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

ValidatorHandler

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

ValidatorHandler

object is created, initially
this field is set to null.

class DraconianErrorHandler implements

ErrorHandler

{
public void fatalError(

SAXParseException

e ) throws

SAXException

{
throw e;
}
public void error(

SAXParseException

e ) throws

SAXException

{
throw e;
}
public void warning(

SAXParseException

e ) throws

SAXException

{
// noop
}
}

When a new

ValidatorHandler

object is created, initially
this field is set to null.

getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

---

#### getErrorHandler

public abstract

ErrorHandler

getErrorHandler()

Gets the current

ErrorHandler

set to this

ValidatorHandler

.

setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

---

#### setResourceResolver

public abstract void setResourceResolver​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution while in a validation episode.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

ValidatorHandler

uses a

LSResourceResolver

when it needs to locate external resources while a validation,
although exactly what constitutes "locating external resources" is
up to each schema language.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbLSResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

class DumbLSResourceResolver implements

LSResourceResolver

{
public

LSInput

resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

ValidatorHandler

will abort the parsing and
the caller of the

validate

method will receive
the same

RuntimeException

.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

When a new

ValidatorHandler

object is created, initially
this field is set to null.

getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

ValidatorHandler

has created.
**See Also:** setErrorHandler(ErrorHandler)

---

#### getResourceResolver

public abstract

LSResourceResolver

getResourceResolver()

Gets the current

LSResourceResolver

set to this

ValidatorHandler

.

getTypeInfoProvider

```java
public abstract
TypeInfoProvider
getTypeInfoProvider()
```

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

**Returns:** null if the validator / schema language does not support
the notion of

TypeInfo

.
Otherwise a non-null valid

TypeInfoProvider

.

---

#### getTypeInfoProvider

public abstract

TypeInfoProvider

getTypeInfoProvider()

Obtains the

TypeInfoProvider

implementation of this

ValidatorHandler

.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

The obtained

TypeInfoProvider

can be queried during a parse
to access the type information determined by the validator.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

Some schema languages do not define the notion of type,
for those languages, this method may not be supported.
However, to be compliant with this specification, implementations
for W3C XML Schema 1.0 must support this operation.

getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setFeature(String, boolean)

---

#### getFeature

public boolean getFeature​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

The feature name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a feature name but
temporarily be unable to return its value.
Some feature values may be available only in specific
contexts, such as before, during, or after a validation.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** getFeature(String)

---

#### setFeature

public void setFeature​(

String

name,
boolean value)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

Set a feature for this

ValidatorHandler

.

Feature can be used to control the way a

ValidatorHandler

parses schemas. The feature name is
any fully-qualified URI. It is possible for a

SchemaFactory

to
expose a feature value but to be unable to change the current
value. Some feature values may be immutable or mutable only in
specific contexts, such as before, during, or after a
validation.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.

false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

ValidatorHandler

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- When

name

is

null

.

---

#### setProperty

public void setProperty​(

String

name,

Object

object)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
to be unable to change the current value.
Some property values may be immutable or mutable only
in specific contexts, such as before, during, or after
a validation.

ValidatorHandler

s are not required to recognize setting
any specific property names.

getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- When

name

is

null

.
**See Also:** setProperty(String, Object)

---

#### getProperty

public

Object

getProperty​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

The property name is any fully-qualified URI. It is
possible for a

ValidatorHandler

to recognize a property name but
temporarily be unable to return its value.
Some property values may be available only in specific
contexts, such as before, during, or after a validation.

ValidatorHandler

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

---

