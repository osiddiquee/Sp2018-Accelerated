from mailroom_oo import Donor, DonorDB

d = Donor('Paul Allen')
d.add_donations(6000)
d2 = Donor('Shigeru Miamoto')
d2.add_donations(9000)
db_test = DonorDB()
db_test.add_donor(d)
db_test.add_donor(d2)

def test_donor_init():
    d = Donor('William Gates III')
    assert d.name == 'William Gates III'
    assert d.donations == []
    d.add_donations(2000)
    d.add_donations(3000)
    assert d.total_donations == 5000


def test_donorDB():
    d = Donor('Paul Allen')
    d.add_donations(6000)
    d2 = Donor('Shigeru Miamoto')
    d2.add_donations(9000)
    db = DonorDB()
    db.add_donor(d)
    db.add_donor(d2)
    assert db.database_dict == {'Paul Allen': [6000], 'Shigeru Miamoto': [9000]}


def test_list_donors():
    listing = ["Donor List:"]
    for donor in db_test.get_donors():
        listing.append(donor)
        test_string =  "\n".join(listing)

    print(listing)
    print(test_string)
    assert listing == ['Donor List:', 'Paul Allen', 'Shigeru Miamoto']
    assert test_string == 'Donor List:\nPaul Allen\nShigeru Miamoto'

def test_find_donor():
    name = 'Paul Allen'
    allen = db_test.database_dict.get(name)
    assert allen == ([6000])


def test_generate_donor_report():
    # First, reduce the raw data into a summary list view
    print(db_test.database_dict)
    report_rows = []
    for (name, gifts) in db_test.database_dict.items():
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append((name, total_gifts, num_gifts, avg_gift))

    # sort the report data
    report_rows.sort(key=lambda x: x[1])
    report = []
    report.append("{:25s} | {:11s} | {:9s} | {:12s}".format("Donor Name",
                                                            "Total Given",
                                                            "Num Gifts",
                                                            "Average Gift"))
    report.append("-" * 66)
    for row in report_rows:
        report.append("{:25s}   ${:10.2f}   {:9d}   ${:11.2f}".format(*row))
    report_final =  "\n".join(report)

    print(report_final)
    assert ('Paul Allen                  $   6000.00           1   $    6000.00'
             in report_final)
