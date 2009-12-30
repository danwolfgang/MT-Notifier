# ===========================================================================
# A Movable Type plugin with subscription options for your installation
# Copyright 2003, 2004, 2005, 2006, 2007 Everitz Consulting <everitz.com>.
#
# This program may not be redistributed without permission.
# ===========================================================================
package Notifier::History;

use strict;

use MT::Object;
@Notifier::History::ISA = qw(MT::Object);
__PACKAGE__->install_properties({
    column_defs => {
        'id' => 'integer not null auto_increment',
        'data_id' => 'integer not null default 0',
        'entry_id' => 'integer not null default 0',
        'comment_id' => 'integer not null default 0',
    },
    indexes => {
        data_id => 1,
        entry_id => 1,
        comment_id => 1,
    },
    audit => 1,
    datasource => 'notifier_history',
    primary_key => 'id',
});

sub class_label {
    MT->translate('Subscription History');
}

sub class_label_plural {
    MT->translate("Subscription History Records");
}

1;
