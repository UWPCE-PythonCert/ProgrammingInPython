#!/usr/bin/env python

"""
Tests for the Command Line interface for mailroom

These require mocking the input() function
"""

from unittest import mock
import pytest

from mailroom.cli import CLI, create_cli_with_sample_data
from mailroom.model import Donor, DonorDB

cli = create_cli_with_sample_data()


@mock.patch('builtins.input')
def test_main_menu_selection(input_mock):
    options = ['1', '2', '3', '4']
    input_mock.side_effect = options
    for o in options:
        ans = cli.main_menu_selection()
        assert ans == o


# my main function doesn't call input
#  but it does call other functions that do
#  so I've mocked those instead.
@mock.patch.object(CLI, 'main_menu_selection')
@mock.patch.object(CLI, 'quit')
def test_main_quit(quit_mock, mms_mock):
    """
    Testing quite independently -not sure why :-)
    but I did this first
    """
    mms_mock.return_value = '4'
    quit_mock.side_effect = RuntimeError
    with pytest.raises(RuntimeError):
        cli.main()
    quit_mock.assert_called_once()


@mock.patch.object(CLI, 'main_menu_selection')
def test_main_invalid(mms_mock):
    mms_mock.side_effect = ["56", "this", "4"]
    with pytest.raises(SystemExit):
        cli.main()
    assert mms_mock.call_count == 3


@mock.patch.object(CLI, 'main_menu_selection')
@mock.patch.object(CLI, 'send_thank_you')
@mock.patch.object(CLI, 'print_donor_report')
@mock.patch.object(DonorDB, 'save_letters_to_disk')
def test_main_send_thanks(sltd_mock, pdr_mock, sty_mock, mms_mock):
    # This runs through each of the menu entries
    #  makes sure the functions are called that are supposed to me
    #  then calls the quit function last
    mms_mock.side_effect = ['1', '2', '3', '4']
    with pytest.raises(SystemExit):
        cli.main()
    pdr_mock.assert_called_once()
    sty_mock.assert_called_once()
    sltd_mock.assert_called_once()


@mock.patch('mailroom.model.DonorDB.generate_donor_report')
def test_print_donor_report(gdr_mock):
    cli.print_donor_report()
    gdr_mock.assert_called_once()


# NOTE: this is pretty complicated to test
#       which means I should probably refactor the code!
#
#       but I'm keeping this here to show how you can test it!
@mock.patch('builtins.input')
def test_send_thank_you_menu(input_mock):
    """ back to menu """
    input_mock.side_effect = ['menu']
    result = cli.send_thank_you()

    assert result is None


@mock.patch('builtins.input')
@mock.patch.object(DonorDB, 'list_donors')
def test_send_thank_you_list(list_mock, input_mock):
    """ list and then menu """
    input_mock.side_effect = ['list', 'menu']
    result = cli.send_thank_you()
    list_mock.assert_called_once()
    assert result is None


@mock.patch('builtins.input')
def test_send_thank_you_name_menu(input_mock):
    """ list and then menu """
    input_mock.side_effect = ["A name", "menu"]
    result = cli.send_thank_you()
    input_mock.assert_called()
    assert input_mock.call_count == 2
    assert result is None


@mock.patch('builtins.input')
@mock.patch.object(DonorDB, 'find_donor')
def test_send_thank_you_new_name(find_mock, input_mock):
    """ list and then menu """
    input_mock.side_effect = ["A name", "5000.0"]
    find_mock.return_value = None
    result = cli.send_thank_you()
    find_mock.assert_called_once()
    assert result is None


@mock.patch('builtins.input')
@mock.patch.object(DonorDB, 'find_donor')
def test_send_thank_you_in_db(find_mock, input_mock):
    """ list and then menu """
    input_mock.side_effect = ["A name", "5000.0"]
    find_mock.return_value = Donor("Test Donor")
    result = cli.send_thank_you()
    find_mock.assert_called_once()
    assert result is None


@mock.patch('builtins.input')
@mock.patch.object(DonorDB, 'find_donor')
def test_send_thank_you_invalid_number(find_mock, input_mock):
    """ list and then menu """
    input_mock.side_effect = ["A name", "not a number", "0.0", "Inf", "1000.0"]
    find_mock.return_value = Donor("Test Donor")
    result = cli.send_thank_you()
    find_mock.assert_called_once()
    assert input_mock.call_count == 5
    assert result is None

