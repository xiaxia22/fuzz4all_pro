# Class ConfirmationCallback

**Source:** `java.base\javax\security\auth\callback\ConfirmationCallback.html`

### Class Description

```java
public class
ConfirmationCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

ConfirmationCallback

to the

handle

method of a

CallbackHandler

to ask for YES/NO,
OK/CANCEL, YES/NO/CANCEL or other similar confirmations.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

#### public static final int UNSPECIFIED_OPTION

Unspecified option type.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

**See Also:**
- Constant Field Values

---

#### public static final int YES_NO_OPTION

YES/NO confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

**See Also:**
- Constant Field Values

---

#### public static final int YES_NO_CANCEL_OPTION

YES/NO/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

**See Also:**
- Constant Field Values

---

#### public static final int OK_CANCEL_OPTION

OK/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

**See Also:**
- Constant Field Values

---

#### public static final int YES

YES option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:**
- Constant Field Values

---

#### public static final int NO

NO option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:**
- Constant Field Values

---

#### public static final int CANCEL

CANCEL option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:**
- Constant Field Values

---

#### public static final int OK

OK option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:**
- Constant Field Values

---

#### public static final int INFORMATION

INFORMATION message type.

**See Also:**
- Constant Field Values

---

#### public static final int WARNING

WARNING message type.

**See Also:**
- Constant Field Values

---

#### public static final int ERROR

ERROR message type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public ConfirmationCallback​(int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:**
- messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
- optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
- defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).

**Throws:**
- IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

---

#### public ConfirmationCallback​(int messageType,

String
[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:**
- messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
- options

- the list of confirmation options.
- defaultOption

- the default option, represented as an index
into the

options

array.

**Throws:**
- IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

---

#### public ConfirmationCallback​(
String
prompt,
int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:**
- prompt

- the prompt used to describe the list of options.
- messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
- optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
- defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).

**Throws:**
- IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

---

#### public ConfirmationCallback​(
String
prompt,
int messageType,

String
[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:**
- prompt

- the prompt used to describe the list of options.
- messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
- options

- the list of confirmation options.
- defaultOption

- the default option, represented as an index
into the

options

array.

**Throws:**
- IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

---

### Method Details

#### public
String
getPrompt()

Get the prompt.

**Returns:**
- the prompt, or null if this

ConfirmationCallback

was instantiated without a

prompt

.

---

#### public int getMessageType()

Get the message type.

**Returns:**
- the message type (

INFORMATION

,

WARNING

or

ERROR

).

---

#### public int getOptionType()

Get the option type.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

**Returns:**
- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

), or

UNSPECIFIED_OPTION

if this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.

---

#### public
String
[] getOptions()

Get the confirmation options.

**Returns:**
- the list of confirmation options, or null if this

ConfirmationCallback

was instantiated with
an

optionType

instead of

options

.

---

#### public int getDefaultOption()

Get the default option.

**Returns:**
- the default option, represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the default option as
an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

---

#### public void setSelectedIndex​(int selection)

Set the selected confirmation option.

**Parameters:**
- selection

- the selection represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor
of this

ConfirmationCallback

.
Otherwise, the selection represents the index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

**See Also:**
- getSelectedIndex()

---

#### public int getSelectedIndex()

Get the selected confirmation option.

**Returns:**
- the selected confirmation option represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the selected confirmation
option as an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

**See Also:**
- setSelectedIndex(int)

---

### Additional Sections

#### Class ConfirmationCallback

java.lang.Object

- javax.security.auth.callback.ConfirmationCallback

javax.security.auth.callback.ConfirmationCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
ConfirmationCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

ConfirmationCallback

to the

handle

method of a

CallbackHandler

to ask for YES/NO,
OK/CANCEL, YES/NO/CANCEL or other similar confirmations.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

ConfirmationCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

ConfirmationCallback

to the

handle

method of a

CallbackHandler

to ask for YES/NO,
OK/CANCEL, YES/NO/CANCEL or other similar confirmations.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CANCEL

CANCEL option.

static int

ERROR

ERROR message type.

static int

INFORMATION

INFORMATION message type.

static int

NO

NO option.

static int

OK

OK option.

static int

OK_CANCEL_OPTION

OK/CANCEL confirmation confirmation option.

static int

UNSPECIFIED_OPTION

Unspecified option type.

static int

WARNING

WARNING message type.

static int

YES

YES option.

static int

YES_NO_CANCEL_OPTION

YES/NO/CANCEL confirmation confirmation option.

static int

YES_NO_OPTION

YES/NO confirmation option.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ConfirmationCallback

​(int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

ConfirmationCallback

​(int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

ConfirmationCallback

​(

String

prompt,
int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

ConfirmationCallback

​(

String

prompt,
int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDefaultOption

()

Get the default option.

int

getMessageType

()

Get the message type.

String

[]

getOptions

()

Get the confirmation options.

int

getOptionType

()

Get the option type.

String

getPrompt

()

Get the prompt.

int

getSelectedIndex

()

Get the selected confirmation option.

void

setSelectedIndex

​(int selection)

Set the selected confirmation option.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

CANCEL

CANCEL option.

static int

ERROR

ERROR message type.

static int

INFORMATION

INFORMATION message type.

static int

NO

NO option.

static int

OK

OK option.

static int

OK_CANCEL_OPTION

OK/CANCEL confirmation confirmation option.

static int

UNSPECIFIED_OPTION

Unspecified option type.

static int

WARNING

WARNING message type.

static int

YES

YES option.

static int

YES_NO_CANCEL_OPTION

YES/NO/CANCEL confirmation confirmation option.

static int

YES_NO_OPTION

YES/NO confirmation option.

---

#### Field Summary

CANCEL option.

ERROR message type.

INFORMATION message type.

NO option.

OK option.

OK/CANCEL confirmation confirmation option.

Unspecified option type.

WARNING message type.

YES option.

YES/NO/CANCEL confirmation confirmation option.

YES/NO confirmation option.

Constructor Summary

Constructors

Constructor

Description

ConfirmationCallback

​(int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

ConfirmationCallback

​(int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

ConfirmationCallback

​(

String

prompt,
int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

ConfirmationCallback

​(

String

prompt,
int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

---

#### Constructor Summary

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDefaultOption

()

Get the default option.

int

getMessageType

()

Get the message type.

String

[]

getOptions

()

Get the confirmation options.

int

getOptionType

()

Get the option type.

String

getPrompt

()

Get the prompt.

int

getSelectedIndex

()

Get the selected confirmation option.

void

setSelectedIndex

​(int selection)

Set the selected confirmation option.

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

Get the default option.

Get the message type.

Get the confirmation options.

Get the option type.

Get the prompt.

Get the selected confirmation option.

Set the selected confirmation option.

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

============ FIELD DETAIL ===========

- Field Detail

- UNSPECIFIED_OPTION

```java
public static final int UNSPECIFIED_OPTION
```

Unspecified option type.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

**See Also:** Constant Field Values

- YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

YES/NO confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

**See Also:** Constant Field Values

- YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

YES/NO/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

**See Also:** Constant Field Values

- OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

OK/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

**See Also:** Constant Field Values

- YES

```java
public static final int YES
```

YES option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- NO

```java
public static final int NO
```

NO option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- CANCEL

```java
public static final int CANCEL
```

CANCEL option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- OK

```java
public static final int OK
```

OK option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- INFORMATION

```java
public static final int INFORMATION
```

INFORMATION message type.

**See Also:** Constant Field Values

- WARNING

```java
public static final int WARNING
```

WARNING message type.

**See Also:** Constant Field Values

- ERROR

```java
public static final int ERROR
```

ERROR message type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

- ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

- ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

- ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

============ METHOD DETAIL ==========

- Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt, or null if this

ConfirmationCallback

was instantiated without a

prompt

.

- getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

- getOptionType

```java
public int getOptionType()
```

Get the option type.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

**Returns:** the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

), or

UNSPECIFIED_OPTION

if this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.

- getOptions

```java
public
String
[] getOptions()
```

Get the confirmation options.

**Returns:** the list of confirmation options, or null if this

ConfirmationCallback

was instantiated with
an

optionType

instead of

options

.

- getDefaultOption

```java
public int getDefaultOption()
```

Get the default option.

**Returns:** the default option, represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the default option as
an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

- setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected confirmation option.

**Parameters:** selection

- the selection represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor
of this

ConfirmationCallback

.
Otherwise, the selection represents the index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** getSelectedIndex()

- getSelectedIndex

```java
public int getSelectedIndex()
```

Get the selected confirmation option.

**Returns:** the selected confirmation option represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the selected confirmation
option as an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** setSelectedIndex(int)

Field Detail

- UNSPECIFIED_OPTION

```java
public static final int UNSPECIFIED_OPTION
```

Unspecified option type.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

**See Also:** Constant Field Values

- YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

YES/NO confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

**See Also:** Constant Field Values

- YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

YES/NO/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

**See Also:** Constant Field Values

- OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

OK/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

**See Also:** Constant Field Values

- YES

```java
public static final int YES
```

YES option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- NO

```java
public static final int NO
```

NO option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- CANCEL

```java
public static final int CANCEL
```

CANCEL option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- OK

```java
public static final int OK
```

OK option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

- INFORMATION

```java
public static final int INFORMATION
```

INFORMATION message type.

**See Also:** Constant Field Values

- WARNING

```java
public static final int WARNING
```

WARNING message type.

**See Also:** Constant Field Values

- ERROR

```java
public static final int ERROR
```

ERROR message type.

**See Also:** Constant Field Values

---

#### Field Detail

UNSPECIFIED_OPTION

```java
public static final int UNSPECIFIED_OPTION
```

Unspecified option type.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

**See Also:** Constant Field Values

---

#### UNSPECIFIED_OPTION

public static final int UNSPECIFIED_OPTION

Unspecified option type.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

The

getOptionType

method returns this
value if this

ConfirmationCallback

was instantiated
with

options

instead of an

optionType

.

YES_NO_OPTION

```java
public static final int YES_NO_OPTION
```

YES/NO confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

**See Also:** Constant Field Values

---

#### YES_NO_OPTION

public static final int YES_NO_OPTION

YES/NO confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

or

NO

.

YES_NO_CANCEL_OPTION

```java
public static final int YES_NO_CANCEL_OPTION
```

YES/NO/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

**See Also:** Constant Field Values

---

#### YES_NO_CANCEL_OPTION

public static final int YES_NO_CANCEL_OPTION

YES/NO/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

YES

,

NO

or

CANCEL

.

OK_CANCEL_OPTION

```java
public static final int OK_CANCEL_OPTION
```

OK/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

**See Also:** Constant Field Values

---

#### OK_CANCEL_OPTION

public static final int OK_CANCEL_OPTION

OK/CANCEL confirmation confirmation option.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

An underlying security service specifies this as the

optionType

to a

ConfirmationCallback

constructor if it requires a confirmation which can be answered
with either

OK

or

CANCEL

.

YES

```java
public static final int YES
```

YES option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

---

#### YES

public static final int YES

YES option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

NO

```java
public static final int NO
```

NO option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

---

#### NO

public static final int NO

NO option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

CANCEL

```java
public static final int CANCEL
```

CANCEL option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

---

#### CANCEL

public static final int CANCEL

CANCEL option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

OK

```java
public static final int OK
```

OK option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

**See Also:** Constant Field Values

---

#### OK

public static final int OK

OK option.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

If an

optionType

was specified to this

ConfirmationCallback

, this option may be specified as a

defaultOption

or returned as the selected index.

INFORMATION

```java
public static final int INFORMATION
```

INFORMATION message type.

**See Also:** Constant Field Values

---

#### INFORMATION

public static final int INFORMATION

INFORMATION message type.

WARNING

```java
public static final int WARNING
```

WARNING message type.

**See Also:** Constant Field Values

---

#### WARNING

public static final int WARNING

WARNING message type.

ERROR

```java
public static final int ERROR
```

ERROR message type.

**See Also:** Constant Field Values

---

#### ERROR

public static final int ERROR

ERROR message type.

Constructor Detail

- ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

- ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

- ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

- ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

---

#### Constructor Detail

ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

---

#### ConfirmationCallback

public ConfirmationCallback​(int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

ConfirmationCallback

```java
public ConfirmationCallback​(int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

---

#### ConfirmationCallback

public ConfirmationCallback​(int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,
int optionType,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** optionType

- the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

).
**Parameters:** defaultOption

- the default option
from the provided optionType (

YES

,

NO

,

CANCEL

or

OK

).
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if optionType is not either

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

, or

OK_CANCEL_OPTION

,
or if

defaultOption

does not correspond to one of the options in

optionType

.

---

#### ConfirmationCallback

public ConfirmationCallback​(

String

prompt,
int messageType,
int optionType,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, an option type and a default option.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

Underlying security services use this constructor if
they require either a YES/NO, YES/NO/CANCEL or OK/CANCEL
confirmation.

ConfirmationCallback

```java
public ConfirmationCallback​(
String
prompt,
int messageType,

String
[] options,
int defaultOption)
```

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

**Parameters:** prompt

- the prompt used to describe the list of options.
**Parameters:** messageType

- the message type (

INFORMATION

,

WARNING

or

ERROR

).
**Parameters:** options

- the list of confirmation options.
**Parameters:** defaultOption

- the default option, represented as an index
into the

options

array.
**Throws:** IllegalArgumentException

- if

prompt

is null,
if

prompt

has a length of 0,
if messageType is not either

INFORMATION

,

WARNING

,
or

ERROR

, if

options

is null,
if

options

has a length of 0,
if any element from

options

is null,
if any element from

options

has a length of 0, or if

defaultOption

does not lie within the array boundaries of

options

.

---

#### ConfirmationCallback

public ConfirmationCallback​(

String

prompt,
int messageType,

String

[] options,
int defaultOption)

Construct a

ConfirmationCallback

with a prompt,
message type, a list of options and a default option.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

Underlying security services use this constructor if
they require a confirmation different from the available preset
confirmations provided (for example, CONTINUE/ABORT or STOP/GO).
The confirmation options are listed in the

options

array,
and are displayed by the

CallbackHandler

implementation
in a manner consistent with the way preset options are displayed.

Method Detail

- getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt, or null if this

ConfirmationCallback

was instantiated without a

prompt

.

- getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

- getOptionType

```java
public int getOptionType()
```

Get the option type.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

**Returns:** the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

), or

UNSPECIFIED_OPTION

if this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.

- getOptions

```java
public
String
[] getOptions()
```

Get the confirmation options.

**Returns:** the list of confirmation options, or null if this

ConfirmationCallback

was instantiated with
an

optionType

instead of

options

.

- getDefaultOption

```java
public int getDefaultOption()
```

Get the default option.

**Returns:** the default option, represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the default option as
an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

- setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected confirmation option.

**Parameters:** selection

- the selection represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor
of this

ConfirmationCallback

.
Otherwise, the selection represents the index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** getSelectedIndex()

- getSelectedIndex

```java
public int getSelectedIndex()
```

Get the selected confirmation option.

**Returns:** the selected confirmation option represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the selected confirmation
option as an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** setSelectedIndex(int)

---

#### Method Detail

getPrompt

```java
public
String
getPrompt()
```

Get the prompt.

**Returns:** the prompt, or null if this

ConfirmationCallback

was instantiated without a

prompt

.

---

#### getPrompt

public

String

getPrompt()

Get the prompt.

getMessageType

```java
public int getMessageType()
```

Get the message type.

**Returns:** the message type (

INFORMATION

,

WARNING

or

ERROR

).

---

#### getMessageType

public int getMessageType()

Get the message type.

getOptionType

```java
public int getOptionType()
```

Get the option type.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

**Returns:** the option type (

YES_NO_OPTION

,

YES_NO_CANCEL_OPTION

or

OK_CANCEL_OPTION

), or

UNSPECIFIED_OPTION

if this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.

---

#### getOptionType

public int getOptionType()

Get the option type.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

If this method returns

UNSPECIFIED_OPTION

, then this

ConfirmationCallback

was instantiated with

options

instead of an

optionType

.
In this case, invoke the

getOptions

method
to determine which confirmation options to display.

getOptions

```java
public
String
[] getOptions()
```

Get the confirmation options.

**Returns:** the list of confirmation options, or null if this

ConfirmationCallback

was instantiated with
an

optionType

instead of

options

.

---

#### getOptions

public

String

[] getOptions()

Get the confirmation options.

getDefaultOption

```java
public int getDefaultOption()
```

Get the default option.

**Returns:** the default option, represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the default option as
an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.

---

#### getDefaultOption

public int getDefaultOption()

Get the default option.

setSelectedIndex

```java
public void setSelectedIndex​(int selection)
```

Set the selected confirmation option.

**Parameters:** selection

- the selection represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor
of this

ConfirmationCallback

.
Otherwise, the selection represents the index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** getSelectedIndex()

---

#### setSelectedIndex

public void setSelectedIndex​(int selection)

Set the selected confirmation option.

getSelectedIndex

```java
public int getSelectedIndex()
```

Get the selected confirmation option.

**Returns:** the selected confirmation option represented as

YES

,

NO

,

OK

or

CANCEL

if an

optionType

was specified to the constructor of this

ConfirmationCallback

.
Otherwise, this method returns the selected confirmation
option as an index into the

options

array specified to the constructor
of this

ConfirmationCallback

.
**See Also:** setSelectedIndex(int)

---

#### getSelectedIndex

public int getSelectedIndex()

Get the selected confirmation option.

---

